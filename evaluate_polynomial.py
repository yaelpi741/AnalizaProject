import matplotlib.pyplot as plt

def evaluate_polynomial(coeffs, x):
    """
    Evaluates a polynomial at a given value x.
    """
    if not coeffs:
        raise ValueError("Coefficient list is empty – cannot evaluate polynomial.")
    result = 0
    degree = len(coeffs) - 1
    for i, coef in enumerate(coeffs):
        if not isinstance(coef, (int, float)):
            raise TypeError(f"Invalid coefficient: {coef} is not a number.")
        result += coef * (x ** (degree - i))
    return result

def trapezoidal_rule(left, right, coeffs, step=0.1, visualize=False):
    """
    Approximates the definite integral of a polynomial using the Trapezoidal Rule.
    Optionally shows a visual plot if visualize=True.
    """
    if step <= 0:
        raise ValueError("Step size must be positive.")
    if left == right:
        return 0.0
    if left > right:
        return -trapezoidal_rule(right, left, coeffs, step, visualize)

    n = int((right - left) / step)
    if n == 0:
        raise ValueError("Interval too small relative to step size – no subintervals created.")

    total_area = 0
    x_vals = []
    y_vals = []

    for i in range(n):
        a = left + i * step
        b = a + step
        fa = evaluate_polynomial(coeffs, a)
        fb = evaluate_polynomial(coeffs, b)
        area = (step / 2) * (fa + fb)
        total_area += area

        if visualize:
            x_vals.extend([a, b])
            y_vals.extend([fa, fb])

    if visualize:
        plot_trapezoids(coeffs, left, right, step, x_vals, y_vals)

    return total_area

def plot_trapezoids(coeffs, left, right, step, x_vals, y_vals):
    """
    Plots the polynomial and trapezoids used in the approximation.
    """
    fine_x = []
    fine_y = []
    x = left
    while x <= right:
        fine_x.append(x)
        fine_y.append(evaluate_polynomial(coeffs, x))
        x += step / 20

    plt.figure(figsize=(10, 5))
    plt.plot(fine_x, fine_y, label='f(x)', color='blue')
    plt.fill_between(fine_x, fine_y, color='lightblue', alpha=0.3)

    # Draw trapezoids
    for i in range(0, len(x_vals) - 1, 2):
        x1, x2 = x_vals[i], x_vals[i + 1]
        y1, y2 = y_vals[i], y_vals[i + 1]
        plt.plot([x1, x1, x2, x2], [0, y1, y2, 0], 'r--', alpha=0.6)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("Trapezoidal Rule Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

"""
def main():
    print("Trapezoidal Rule Integration for a Polynomial Function")
    try:
        # Read polynomial coefficients
        raw_input = input("Enter polynomial coefficients (from highest degree to constant, space-separated):\n")
        coeffs = [float(c) for c in raw_input.strip().split()]

        # Read integration bounds
        a = float(input("Enter left boundary (a): "))
        b = float(input("Enter right boundary (b): "))

        # Read step size
        step = float(input("Enter step size (e.g., 0.1): "))

        # Perform integration and visualize
        result = trapezoidal_rule(a, b, coeffs, step, visualize=True)
        print(f"\nApproximate value of the definite integral: {result:.6f}")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
"""
