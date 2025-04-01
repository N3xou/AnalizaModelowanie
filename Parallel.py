import threading
import random
import time


# Merge function for merging two sorted halves
def merge(array, left, middle, right):
    leftPart = array[left:middle + 1]
    rightPart = array[middle + 1:right + 1]
    i = j = k = left

    # Merging the left and right parts into the original array
    while i < len(leftPart) and j < len(rightPart):
        if leftPart[i] <= rightPart[j]:
            array[k] = leftPart[i]
            i += 1
        else:
            array[k] = rightPart[j]
            j += 1
        k += 1

    # Copy remaining elements from left part if any
    while i < len(leftPart):
        array[k] = leftPart[i]
        i += 1
        k += 1

    # Copy remaining elements from right part if any
    while j < len(rightPart):
        array[k] = rightPart[j]
        j += 1
        k += 1


# Parallel Merge Sort function using threads
def parallelMergeSort(array, left, right, depth=0):
    if left >= right:
        return

    middle = left + (right - left) // 2

    if depth < 4:
        # Create threads for parallel sorting of both halves
        thread1 = threading.Thread(target=parallelMergeSort, args=(array, left, middle, depth + 1))
        thread2 = threading.Thread(target=parallelMergeSort, args=(array, middle + 1, right, depth + 1))

        thread1.start()
        thread2.start()

        # Wait for both threads to complete
        thread1.join()
        thread2.join()
    else:
        # If the depth reaches 4, no more threads, just recursively call mergeSort
        parallelMergeSort(array, left, middle, depth + 1)
        parallelMergeSort(array, middle + 1, right, depth + 1)

    # Merge the sorted halves
    merge(array, left, middle, right)


# Main function
def main():
    # Generating a random array of numbers
    data_array = [random.randint(0, 1000) for _ in range(100000)]

    # Start timing using perf_counter for high precision
    start_time = time.perf_counter()

    # Run the parallel merge sort
    parallelMergeSort(data_array, 0, len(data_array) - 1)

    # End timing
    end_time = time.perf_counter()

    # Calculate and display the elapsed time
    elapsed_time = end_time - start_time
    print(f"Execution time of parallel merge sort: {elapsed_time*100:.6f} ms")
    # Optionally, print the sorted array (might be large)
    # print(f"Sorted array: {data_array[:100]}...")


if __name__ == "__main__":
    main()
