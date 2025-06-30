import matplotlib.pyplot as plt

def cubic_spline_interpolation(x_vals, y_vals, x_target):
    """
    Performs cubic spline interpolation on a set of known data points.
    Returns the interpolated y-value at x_target.
    """
    n = len(x_vals)

    if n != len(y_vals):
        raise ValueError("The number of X values must match the number of Y values.")
    if n < 3:
        raise ValueError("At least 3 points are required for cubic spline interpolation.")
    if any(x_vals[i] >= x_vals[i + 1] for i in range(n - 1)):
        raise ValueError("X values must be strictly increasing.")
    if x_target < x_vals[0] or x_target > x_vals[-1]:
        raise ValueError(f"x_target ({x_target}) out of bounds.")

    # Step 1: Calculate h and alpha
    h = [x_vals[i + 1] - x_vals[i] for i in range(n - 1)]
    alpha = [0] * n
    for i in range(1, n - 1):
        alpha[i] = (3 / h[i]) * (y_vals[i + 1] - y_vals[i]) - (3 / h[i - 1]) * (y_vals[i] - y_vals[i - 1])

    # Step 2: Tridiagonal solver
    l = [1] + [0] * (n - 1)
    mu = [0] * n
    z = [0] * n
    for i in range(1, n - 1):
        l[i] = 2 * (x_vals[i + 1] - x_vals[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
    l[-1] = 1
    z[-1] = 0

    # Step 3: Back-substitution
    c = [0] * n
    b = [0] * (n - 1)
    d = [0] * (n - 1)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y_vals[j + 1] - y_vals[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Step 4: Evaluate the spline at x_target
    for i in range(n - 1):
        if x_vals[i] <= x_target <= x_vals[i + 1]:
            dx = x_target - x_vals[i]
            y_interp = y_vals[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
            return y_interp, b, c, d

    raise RuntimeError("No interval found for x_target.")

def linspace(start, stop, num):
    """
    Replacement for numpy.linspace without using numpy.
    Returns a list of 'num' evenly spaced values between start and stop.
    """
    if num == 1:
        return [start]
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]

def plot_spline(x_vals, y_vals, b, c, d, x_target, y_interp):
    """
    Plots the cubic spline curve and interpolated point.
    """
    x_plot = linspace(x_vals[0], x_vals[-1], 500)
    y_plot = []

    for x in x_plot:
        for i in range(len(x_vals) - 1):
            if x_vals[i] <= x <= x_vals[i + 1]:
                dx = x - x_vals[i]
                y = y_vals[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
                y_plot.append(y)
                break

    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, label="Cubic Spline", color='blue')
    plt.scatter(x_vals, y_vals, color='red', label="Data Points")
    plt.scatter(x_target, y_interp, color='green', label=f"Interpolated Point ({x_target:.2f}, {y_interp:.2f})")
    plt.title("Cubic Spline Interpolation (No NumPy)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    try:
        print("Cubic Spline Interpolation (No NumPy)")
        x_vals = [1, 2, 3, 4]
        y_vals = [1, 4, 9, 16]
        x_target = float(input("Enter x value to interpolate: "))

        y_interp, b, c, d = cubic_spline_interpolation(x_vals, y_vals, x_target)
        print(f"Estimated value at x = {x_target}: {y_interp:.6f}")
        plot_spline(x_vals, y_vals, b, c, d, x_target, y_interp)

    except ValueError as ve:
        print("ValueError:", str(ve))
    except RuntimeError as re:
        print("RuntimeError:", str(re))
    except Exception as e:
        print("Unexpected error:", str(e))

if __name__ == "__main__":
    main()
