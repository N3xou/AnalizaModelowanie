import tkinter as tk
import time
import statistics

response_times = []  # List to store button response times
calculation_times = []  # List to store calculation times

# Open a text file to save results
txt_file = open("calculator_times.txt", "w")

def on_close():
    global close_time
    if 'close_time' not in globals():  # Ensure it runs only once
        root.destroy()
        close_time = time.perf_counter()
        total_runtime = close_time - start_time
        print(f"Time from pressing X to closing: {close_time*100 - x_press_time*100:.6f} ms")
        #print(f"Total app runtime: {total_runtime:.6f} seconds")
        if response_times:
            median_response_time = statistics.median(response_times)
            print(f"Median response time for number buttons: {median_response_time*100:.6f} ms")
        if calculation_times:
            median_calculation_time = statistics.median(calculation_times)
            print(f"Median calculation time: {median_calculation_time*100:.6f} ms")

        # Save results to the text file
        txt_file.write(f"{load_time*100 - start_time*100:.6f}\n") # time for starting window
        txt_file.write(f"{close_time*100 - x_press_time*100:.6f}\n")  # Time from X press to closing
        #txt_file.write(f"{total_runtime:.6f}\n")  # Total app runtime
        txt_file.write(f"{statistics.median(response_times*100) if response_times else 'N/A':.6f}\n")  # Median response time
        txt_file.write(f"{statistics.median(calculation_times*100) if calculation_times else 'N/A':.6f}\n")  # Median calculation time





def on_x_press():
    global x_press_time
    if 'x_press_time' not in globals() or x_press_time == 0:
        x_press_time = time.perf_counter()
    on_close()

def on_click(event):
    start = time.perf_counter()
    text = event.widget.cget("text")
    if text.isdigit():  # Measure response time only for number buttons
        entry_var.set(entry_var.get() + text)
        end = time.perf_counter()
        response_times.append(end - start)
    elif text == "=":
        start_calc = time.perf_counter()
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
        end_calc = time.perf_counter()
        calculation_times.append(end_calc - start_calc)
    elif text == "C":
        entry_var.set("")
    elif text in ['+', '-', '*', '/']:  # Handle operator buttons
        entry_var.set(entry_var.get() + text)

# Create main window
start_time = time.perf_counter()
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

load_time = time.perf_counter()
print(f"Time taken to open the window: {load_time*100 - start_time*100:.6f} ms")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for char in row:
        btn = tk.Button(row_frame, text=char, font=("Arial", 18), relief=tk.GROOVE, height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", on_click)

x_press_time = 0
root.protocol("WM_DELETE_WINDOW", on_x_press)

root.mainloop()

# Close the text file after the application closes
txt_file.close()
