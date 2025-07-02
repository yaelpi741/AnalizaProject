import math
import matplotlib.pyplot as plt

def romberg(f, a, b, max_level, verbose=True, real_value=None):
    R = [[0.0] * (i + 1) for i in range(max_level)]
    h = b - a
    R[0][0] = 0.5 * h * (f(import math
import matplotlib.pyplot as plt

def romberg(f, a, b, max_level, verbose=True, real_value=None):
    R = [[0.0] * (i + 1) for i in range(max_level)]
    h = b - a
    R[0][0] = 0.5 * h * (f(a) + f(b))

    for i in range(1, max_level):
        h /= 2.0
        subtotal = sum(f(a + (2 * k - 1) * h) for k in range(1, 2**(i - 1) + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * subtotal
        for j in range(1, i + 1):
            R[i][j] = (4**j * R[i][j - 1] - R[i - 1][j - 1]) / (4**j - 1)

    if verbose:
        print("\nRomberg Integration Table:")
        for i in range(max_level):
            row = ["{:.10f}".format(R[i][j]) for j in range(i + 1)]
            print(f"R[{i}]: {row}")

        if real_value is not None:
            approx = R[max_level - 1][max_level - 1]
            error = abs(approx - real_value)
            print(f"\nEstimated value: {approx:.10f}")
            print(f"Absolute error: {error:.10e}")

        if real_value is not None:
            plot_romberg_convergence(R, real_value)

    return R, R[max_level - 1][max_level - 1]

def plot_romberg_convergence(R, real_value):
    approx_values = [R[i][i] for i in range(len(R))]  # Diagonal values
    levels = list(range(1, len(R) + 1))

    plt.figure()
    plt.plot(levels, approx_values, marker='o', label='Romberg Approximation')
    plt.axhline(real_value, color='green', linestyle='--', label=f'True Value ≈ {real_value:.10f}')
    plt.xlabel('Refinement Level')
    plt.ylabel('Approximation')
    plt.title('Romberg Convergence Plot')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def select_function(choice):
    if choice == "1":
        return lambda x: math.sin(x), "sin(x)", 2.0
    elif choice == "2":
        return lambda x: x**2, "x^2", None
    elif choice == "3":
        return lambda x: math.exp(x), "exp(x)", None
    else:
        raise ValueError("Invalid function choice")

"""
if __name__ == "__main__":
    print("Romberg Integration - User Input Mode")

    print("Choose a function to integrate:")
    print("1. sin(x)     from 0 to pi        (expected = 2.0)")
    print("2. x^2        from a to b         (expected = (b^3 - a^3)/3)")
    print("3. exp(x)     from a to b         (expected = e^b - e^a)")

    func_choice = input("Enter your choice (1/2/3): ").strip()
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    max_level = int(input("Enter number of refinement levels (e.g., 4 or 5): "))

    try:
        f, fname, true_val = select_function(func_choice)

        if true_val is None:
            if func_choice == "2":
                true_val = (b**3 - a**3) / 3
            elif func_choice == "3":
                true_val = math.exp(b) - math.exp(a)

        print(f"\nIntegrating {fname} from {a} to {b} with {max_level} levels...")

        romberg(f, a, b, max_level=max_level, real_value=true_val)

    except ValueError as ve:
        print("Error:", ve)
"""
from math import sin, cos, exp
import numpy as np
import matplotlib.pyplot as plt

def romberg_main():
    print("Running Romberg Integration...")
    def f(x):
        return eval(select_function())
    a = float(input("Enter start of interval a: "))
    b = float(input("Enter end of interval b: "))
    n = int(input("Enter number of iterations: "))
    result, matrix = romberg(f, a, b, n)
    print("Result:", result)
    plot_romberg_convergence(matrix)
a) + f(b))

    for i in range(1, max_level):
        h /= 2.0
        subtotal = sum(f(a + (2 * k - 1) * h) for k in range(1, 2**(i - 1) + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * subtotal
        for j in range(1, i + 1):
            R[i][j] = (4**j * R[i][j - 1] - R[i - 1][j - 1]) / (4**j - 1)

    if verbose:
        print("\nRomberg Integration Table:")
        for i in range(max_level):
            row = ["{:.10f}".format(R[i][j]) for j in range(i + 1)]
            print(f"R[{i}]: {row}")

        if real_value is not None:
            approx = R[max_level - 1][max_level - 1]
            error = abs(approx - real_value)
            print(f"\nEstimated value: {approx:.10f}")
            print(f"Absolute error: {error:.10e}")

        if real_value is not None:
            plot_romberg_convergence(R, real_value)

    return R, R[max_level - 1][max_level - 1]

def plot_romberg_convergence(R, real_value):
    approx_values = [R[i][i] for i in range(len(R))]  # Diagonal values
    levels = list(range(1, len(R) + 1))

    plt.figure()
    plt.plot(levels, approx_values, marker='o', label='Romberg Approximation')
    plt.axhline(real_value, color='green', linestyle='--', label=f'True Value ≈ {real_value:.10f}')
    plt.xlabel('Refinement Level')
    plt.ylabel('Approximation')
    plt.title('Romberg Convergence Plot')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def select_function(choice):
    if choice == "1":
        return lambda x: math.sin(x), "sin(x)", 2.0
    elif choice == "2":
        return lambda x: x**2, "x^2", None
    elif choice == "3":
        return lambda x: math.exp(x), "exp(x)", None
    else:
        raise ValueError("Invalid function choice")

if __name__ == "__main__":
    print("Romberg Integration - User Input Mode")

    print("Choose a function to integrate:")
    print("1. sin(x)     from 0 to pi        (expected = 2.0)")
    print("2. x^2        from a to b         (expected = (b^3 - a^3)/3)")
    print("3. exp(x)     from a to b         (expected = e^b - e^a)")

    func_choice = input("Enter your choice (1/2/3): ").strip()
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    max_level = int(input("Enter number of refinement levels (e.g., 4 or 5): "))

    try:
        f, fname, true_val = select_function(func_choice)

        if true_val is None:
            if func_choice == "2":
                true_val = (b**3 - a**3) / 3
            elif func_choice == "3":
                true_val = math.exp(b) - math.exp(a)

        print(f"\nIntegrating {fname} from {a} to {b} with {max_level} levels...")

        romberg(f, a, b, max_level=max_level, real_value=true_val)

    except ValueError as ve:
        print("Error:", ve)
