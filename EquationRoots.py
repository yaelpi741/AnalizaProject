# Yael Pinto - 326252376
# Shahar Ezra - 329186118
# Tamar Mosheev - 213864242

import matplotlib.pyplot as plt

def f(x):
    """Returns the value of the function f(x) = x^3 - 6x^2 + 11x - 6."""
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    """Returns the derivative f'(x) = 3x^2 - 12x + 11."""
    return 3*x**2 - 12*x + 11

def newton_raphson(func, dfunc, x0, epsilon=0.0001, max_iterations=100):
    iterations = 0
    while iterations < max_iterations:
        fx = func(x0)
        dfx = dfunc(x0)
        if dfx == 0:
            print("Derivative is zero. Method failed to converge.")
            return None, iterations
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < epsilon:
            return x1, iterations + 1
        x0 = x1
        iterations += 1
    print("Method did not converge.")
    return None, iterations

def secant_method(func, start_point, end_point, epsilon=0.0001, max_iterations=100):
    x0 = start_point
    x1 = end_point
    iteration = 0

    if x0 == x1:
        print(f"[Secant] Invalid input: start_point and end_point are the same ({x0}).")
        return None, iteration

    while iteration < max_iterations:
        try:
            f_x0 = func(x0)
            f_x1 = func(x1)
        except Exception as e:
            print(f"[Secant] Error evaluating function at iteration {iteration}: {e}")
            return None, iteration

        if abs(f_x0) < epsilon:
            print(f"[Secant] Exact root found at x = {x0}")
            return x0, iteration
        if abs(f_x1) < epsilon:
            print(f"[Secant] Exact root found at x = {x1}")
            return x1, iteration

        denominator = f_x1 - f_x0
        if denominator == 0:
            print(f"[Secant] Division by zero detected at iteration {iteration}. f(x1) - f(x0) = 0.")
            return None, iteration

        x2 = x1 - f_x1 * (x1 - x0) / denominator

        if abs(x2 - x1) < epsilon:
            return x2, iteration + 1

        x0, x1 = x1, x2
        iteration += 1

    print(f"[Secant] Method did not converge within {max_iterations} iterations.")
    return None, iteration

def bisection_method(f, start, end, epsilon=0.0001):
    a = start
    b = end
    iterations = 0
    if f(a) * f(b) >= 0:
        print("Function does not change sign in the interval.")
        return None, iterations
    while (b - a) / 2.0 > epsilon:
        iterations += 1
        mid = (a + b) / 2.0
        f_mid = f(mid)
        if abs(f_mid) < epsilon:
            return mid, iterations
        elif f(a) * f_mid < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2.0, iterations

def plot_function_with_roots(f, roots, start, end, step=0.01, method_name=""):
    """
    Plots the function f(x) and highlights the roots found.
    """
    x_vals = []
    y_vals = []

    x = start
    while x <= end:
        x_vals.append(x)
        y_vals.append(f(x))
        x += step

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)

    if roots:
        for root in roots:
            plt.scatter(root, f(root), color='green', label=f'Root at x={root:.4f}')
        plt.title(f"{method_name} - Roots Visualization")
    else:
        plt.title(f"{method_name} - No roots found")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    start = 0
    end = 4
    step = 0.1
    epsilon = 0.0001

    while True:
        print("\nChoose method to find roots:")
        print("1 - Bisection Method")
        print("2 - Newton-Raphson Method")
        print("3 - Secant Method")
        print("0 - Exit")
        choice = input("Enter your choice (0/1/2/3): ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            print("\nUsing Bisection Method...")
            index = 1
            roots = []
            found = False
            x = start
            while x < end:
                if f(x) * f(x + step) < 0 or df(x) * df(x + step) < 0:
                    root, iterations = bisection_method(f, x, x + step, epsilon)
                    if root is not None:
                        print(f"Root {index}: {root} (Iterations: {iterations})")
                        roots.append(root)
                        index += 1
                        found = True
                x += step
            if not found:
                print("No root found in the given interval using Bisection Method.")
            plot_function_with_roots(f, roots, start, end, method_name="Bisection Method")

        elif choice == "2":
            print("\nUsing Newton-Raphson Method...")
            index = 1
            roots = []
            found = False
            x = start
            while x < end:
                if f(x) * f(x + step) < 0 or df(x) * df(x + step) < 0:
                    mid = (x + x + step) / 2
                    root, iterations = newton_raphson(f, df, mid, epsilon)
                    if root is not None:
                        print(f"Root {index}: {root} (Iterations: {iterations})")
                        roots.append(root)
                        index += 1
                        found = True
                x += step
            if not found:
                print("No root found in the given interval using Newton-Raphson Method.")
            plot_function_with_roots(f, roots, start, end, method_name="Newton-Raphson Method")

        elif choice == "3":
            print("\nUsing Secant Method...")
            index = 1
            roots = []
            found = False
            x = start
            while x < end:
                if f(x) * f(x + step) < 0 or df(x) * df(x + step) < 0:
                    root, iterations = secant_method(f, x, x + step, epsilon)
                    if root is not None:
                        print(f"Root {index}: {root} (Iterations: {iterations})")
                        roots.append(root)
                        index += 1
                        found = True
                x += step
            if not found:
                print("No root found in the given interval using Secant Method.")
            plot_function_with_roots(f, roots, start, end, method_name="Secant Method")

        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")

main()
