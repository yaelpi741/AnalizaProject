import matplotlib.pyplot as plt

def lagrange_interpolation(x_vals, y_vals, x_interp):
    """
    Performs Lagrange interpolation to estimate the value of a function at a given point.

    Parameters:
        x_vals (list of float): x-coordinates of the data points.
        y_vals (list of float): y-coordinates of the data points.
        x_interp (float): The x-value where interpolation is desired.

    Returns:
        float: The interpolated y-value.
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y lists must be of the same length.")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required.")

    n = len(x_vals)
    result = 0.0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                denominator = x_vals[i] - x_vals[j]
                if denominator == 0:
                    raise ZeroDivisionError("Duplicate X values detected.")
                term *= (x_interp - x_vals[j]) / denominator
        result += term
    return result

def neville_interpolation(x_vals, y_vals, x_interp):
    """
    Performs Neville's method to estimate the value of a function at a given point.

    Parameters:
        x_vals (list of float): x-coordinates of the data points.
        y_vals (list of float): y-coordinates of the data points.
        x_interp (float): The x-value where interpolation is desired.

    Returns:
        float: The interpolated y-value.
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y lists must be of the same length.")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required.")

    n = len(x_vals)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Q[i][0] = y_vals[i]

    for j in range(1, n):
        for i in range(n - j):
            denominator = x_vals[i] - x_vals[i + j]
            if denominator == 0:
                raise ZeroDivisionError("Duplicate X values detected in Neville's method.")
            Q[i][j] = ((x_interp - x_vals[i + j]) * Q[i][j - 1] +
                       (x_vals[i] - x_interp) * Q[i + 1][j - 1]) / denominator

    return Q[0][n - 1]

def plot_interpolation(x_vals, y_vals, x_interp, y_interp):
    """
    Plots the interpolation result along with the original data points and the interpolation curve.

    Parameters:
        x_vals (list of float): x-coordinates of the data points.
        y_vals (list of float): y-coordinates of the data points.
        x_interp (float): The x-value where interpolation is desired.
        y_interp (float): The interpolated y-value to be shown on the plot.
    """
    x_range = []
    current = min(x_vals) - 0.5
    end = max(x_vals) + 0.5
    step = 0.01
    while current <= end:
        x_range.append(current)
        current += step

    y_range = [lagrange_interpolation(x_vals, y_vals, xi) for xi in x_range]

    plt.figure()
    plt.plot(x_range, y_range, label='Lagrange Polynomial', color='blue')
    plt.plot(x_vals, y_vals, 'ro', label='Original Points')
    plt.plot(x_interp, y_interp, 'gs', label=f'Interpolated Point ({x_interp:.2f}, {y_interp:.2f})')

    plt.title('Polynomial Interpolation (Lagrange)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to perform interpolation using Lagrange and Neville methods.
    It receives user input and displays results and plots.
    """
    try:
        n = int(input("How many data points? "))
        x = []
        y = []

        print("Enter the points as two numbers separated by space (x y):")
        for i in range(n):
            pair = input(f"Point {i+1}: ").strip().split()
            if len(pair) != 2:
                raise ValueError("Each point must contain exactly two numbers.")
            xi = float(pair[0])
            yi = float(pair[1])
            x.append(xi)
            y.append(yi)

        x_interp = float(input("Enter the x-value to interpolate: "))

        y_lagrange = lagrange_interpolation(x, y, x_interp)
        print(f"Lagrange interpolation at x = {x_interp}: y ≈ {y_lagrange:.4f}")

        y_neville = neville_interpolation(x, y, x_interp)
        print(f"Neville interpolation at x = {x_interp}: y ≈ {y_neville:.4f}")

        plot_interpolation(x, y, x_interp, y_lagrange)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
