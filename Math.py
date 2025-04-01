import random
import math
import time

# Funkcja f(x), którą będziemy całkować
def f(x):
    return x ** 2


# Metoda trapezów
def Integrate_Trapezoidal(f, a, b, n):
    h = (b - a) / n  # Krok podziału
    total_sum = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        total_sum += (f(x1) + f(x2)) / 2 * h
    return total_sum


# Metoda Simpsona
def Integrate_Simpson(f, a, b, n):
    if n % 2 == 1:  # Simpson wymaga liczby parzystej
        n = n + 1
    h = (b - a) / n
    total_sum = f(a) + f(b)

    # Suma dla nieparzystych indeksów
    for i in range(1, n, 2):
        x = a + i * h
        total_sum += 4 * f(x)

    # Suma dla parzystych indeksów
    for i in range(2, n, 2):
        x = a + i * h
        total_sum += 2 * f(x)

    return (h / 3) * total_sum


# Metoda Monte Carlo
def Integrate_MonteCarlo(f, a, b, n):
    m = 0  # Licznik punktów pod wykresem
    max_f = max(f(a), f(b))  # Maksimum funkcji na przedziale
    for i in range(n):
        x = random.uniform(a, b)  # Losowanie x z przedziału [a, b]
        y = random.uniform(0, max_f)  # Losowanie y z przedziału [0, max(f)]

        if y <= f(x):  # Punkt znajduje się pod wykresem funkcji
            m += 1

    return (m / n) * (b - a) * max_f


# Funkcja główna
def main():
    a = 0  # Początek przedziału
    b = 1  # Koniec przedziału
    n = 1000  # Liczba podziałów

    # Pomiar czasu dla metody trapezów
    start_time = time.perf_counter()
    trapezoidal_result = Integrate_Trapezoidal(f, a, b, n)
    end_time = time.perf_counter()
    trapezoidal_time = end_time - start_time

    # Pomiar czasu dla metody Simpsona
    start_time = time.perf_counter()
    simpson_result = Integrate_Simpson(f, a, b, n)
    end_time = time.perf_counter()
    simpson_time = end_time - start_time

    # Pomiar czasu dla metody Monte Carlo
    start_time = time.perf_counter()
    montecarlo_result = Integrate_MonteCarlo(f, a, b, n)
    end_time = time.perf_counter()
    montecarlo_time = end_time - start_time

    # Wyświetlanie wyników
    print(f"Metoda trapezów wynik calki: {trapezoidal_result:.4f} (czas: {trapezoidal_time*100:.6f} ms)")
    print(f"Metoda Simpsona wynik calki: {simpson_result:.4f} (czas: {simpson_time*100:.6f} ms)")
    print(f"Metoda Monte Carlo wynik calki: {montecarlo_result:.4f} (czas: {montecarlo_time*100:.6f} ms)")

# Uruchomienie programu
if __name__ == "__main__":
    main()
