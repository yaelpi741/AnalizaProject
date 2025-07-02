import math
import matplotlib.pyplot as plt

def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule.")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n, 2):
        total += 4 * f(a + i * h)

    for i in range(2, n, 2):
        total += 2 * f(a + i * h)

    return (h / 3) * total

def select_function(choice):
    if choice == "1":
        return lambda x: math.sin(x), "sin(x)", 2.0
    elif choice == "2":
        return lambda x: x ** 2, "x^2", None
    elif choice == "3":
        return lambda x: math.exp(x), "exp(x)", None
    else:
        raise ValueError("Invalid function choice")

def plot_convergence(f, a, b, exact, fname):
    ns = list(range(2, 32, 2))  # Even values of n from 2 to 30
    approximations = [simpson(f, a, b, n) for n in ns]
    errors = [abs(approx - exact) for approx in approximations]

    plt.figure()
    plt.plot(ns, approximations, 'bo-', label='Simpson Approximation')
    plt.axhline(y=exact, color='green', linestyle='--', label=f'Exact Value ≈ {exact:.10f}')
    plt.xlabel('Number of Subintervals (n)')
    plt.ylabel('Integral Approximation')
    plt.title(f'Simpson’s Rule Convergence – f(x) = {fname}')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("Simpson’s Rule – Numerical Integration\n")

    print("Choose a function to integrate:")
    print("1. sin(x)     from 0 to pi        (expected ≈ 2.0)")
    print("2. x^2        from a to b         (expected = (b^3 - a^3)/3)")
    print("3. exp(x)     from a to b         (expected = e^b - e^a)")

    choice = input("Enter your choice (1/2/3): ").strip()
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    n = int(input("Enter number of subintervals (even number): "))

    if n % 2 != 0:
        print("Number of subintervals must be even. Exiting.")
        return

    try:
        f, fname, true_val = select_function(choice)

        if true_val is None:
            if choice == "2":
                true_val = (b ** 3 - a ** 3) / 3
            elif choice == "3":
                true_val = math.exp(b) - math.exp(a)

        approx = simpson(f, a, b, n)

        print(f"\nIntegrating {fname} from {a} to {b} using {n} subintervals.")
        print(f"Approximate integral: {approx:.10f}")
        if true_val is not None:
            error = abs(approx - true_val)
            print(f"Exact value:          {true_val:.10f}")
            print(f"Absolute error:       {error:.10e}")

            # Show convergence plot
            plot_convergence(f, a, b, true_val, fname)

    except ValueError as e:
        print("Error:", e)
"""
if __name__ == "__main__":
    main()
"""
