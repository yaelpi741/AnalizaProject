import matplotlib.pyplot as plt

def forward_elimination(A, b):
    """
    Performs the forward phase of Gaussian Elimination:
    transforms matrix A into upper-triangular form and updates vector b.

    Parameters:
        A (list of list of float): Square coefficient matrix (n x n).
        b (list of float): Right-hand side vector (length n).

    Returns:
        tuple: (Upper-triangular matrix A, modified RHS vector b)

    Raises:
        ValueError: If matrix is not square, vector size mismatch,
                    or zero pivot (division by zero).
    """
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("Matrix A must be square.")
    if len(b) != n:
        raise ValueError("Vector b length must match matrix A size.")

    # Deep copy to avoid modifying input directly
    A = [row[:] for row in A]
    b = b[:]

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError(f"Zero pivot encountered at row {i}. Try row swapping (pivoting).")

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    return A, b

def back_substitution(U, y):
    """
    Performs back-substitution to solve Ux = y,
    where U is upper-triangular.

    Parameters:
        U (list of list of float): Upper-triangular matrix (n x n).
        y (list of float): Updated RHS vector from forward elimination.

    Returns:
        list of float: Solution vector x.

    Raises:
        ValueError: If zero diagonal element is found (division by zero).
    """
    n = len(U)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ValueError(f"Zero diagonal element at row {i}, cannot divide.")

        sum_ = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_) / U[i][i]

    return x

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination (no pivoting).

    Parameters:
        A (list of list of float): Coefficient matrix.
        b (list of float): Right-hand side vector.

    Returns:
        list of float: Solution vector x.
    """
    U, y = forward_elimination(A, b)
    return back_substitution(U, y)

def plot_solution(x):
    """
    Plots the solution vector x as a bar chart.

    Parameters:
        x (list of float): Solution vector to be plotted.
    """
    indices = list(range(len(x)))
    plt.bar(indices, x)
    plt.xlabel("Variable Index")
    plt.ylabel("Value")
    plt.title("Solution Vector x")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def get_matrix_input():
    """
    Prompts the user to input matrix A and vector b interactively.

    Returns:
        tuple: (A, b) where:
            - A is a list of lists (matrix)
            - b is a list (vector)

    Raises:
        ValueError: If input dimensions are invalid or inconsistent.
    """
    n = int(input("Enter number of variables (n): "))
    A = []
    for i in range(n):
        row_input = input(f"Enter row {i + 1} (space-separated): ")
        row = [float(val) for val in row_input.strip().split()]
        if len(row) != n:
            raise ValueError(f"Row {i + 1} must contain exactly {n} values.")
        A.append(row)

    b_input = input("Enter RHS vector b (space-separated): ")
    b = [float(val) for val in b_input.strip().split()]
    if len(b) != n:
        raise ValueError("Vector b length must match number of variables.")

    return A, b

def trapezoid_rule(f, a, b, n):
    """
    Approximates the definite integral of a function f over [a, b]
    using the Trapezoidal Rule with n subintervals.

    Parameters:
        f (function): The integrand – a function of one variable.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): Number of subintervals (must be >= 1).

    Returns:
        float: Approximation of the integral of f from a to b.

    Raises:
        ValueError: If n < 1 or a >= b.
    """
    if n < 1:
        raise ValueError("Number of subintervals n must be at least 1.")
    if a >= b:
        raise ValueError("Lower limit a must be less than upper limit b.")

    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))  # Endpoints are halved
    for i in range(1, n):
        total += f(a + i * h)

    return h * total


"""
def main():
    """
"""
    Main program flow:
    - Gets input matrix and vector from user
    - Solves using Gaussian Elimination
    - Displays result and (optionally) shows a bar chart of the solution
    """
"""
    try:
        print("Gaussian Elimination Solver")
        A, b = get_matrix_input()
        x = gaussian_elimination(A, b)

        print("\nSolution vector x:")
        for i, val in enumerate(x):
            print(f"x[{i}] = {val:.4f}")

        plot = input("\nShow bar chart of solution? (y/n): ").strip().lower()
        if plot == 'y':
            plot_solution(x)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
"""
