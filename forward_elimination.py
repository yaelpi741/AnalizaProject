import matplotlib.pyplot as plt

def forward_elimination(A, b):
    """
    Performs the forward phase of Gaussian Elimination.

    Parameters:
        A (list of list of float): Coefficient matrix (must be square).
        b (list of float): Right-hand side vector.

    Returns:
        tuple: (Upper-triangular matrix A, updated RHS vector b).

    Raises:
        ValueError: If matrix is not square, mismatched vector size,
                    or a zero pivot is encountered.
    """
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("Matrix A must be square.")
    if len(b) != n:
        raise ValueError("Vector b length must match matrix A size.")

    A = [row[:] for row in A]  # deep copy
    b = b[:]

    for i in range(n):
        if A[i][i] == 0:
            raise ValueError(f"Zero pivot encountered at row {i}. Try pivoting.")

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    return A, b

def back_substitution(U, y):
    """
    Performs the backward phase to solve Ux = y.

    Parameters:
        U (list of list of float): Upper-triangular matrix.
        y (list of float): RHS vector after forward elimination.

    Returns:
        list of float: Solution vector x.

    Raises:
        ValueError: If diagonal element is zero (division by zero).
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
    Solves a system Ax = b using Gaussian Elimination (no pivoting).

    Parameters:
        A (list of list of float): Coefficient matrix.
        b (list of float): RHS vector.

    Returns:
        list of float: Solution vector x.
    """
    U, y = forward_elimination(A, b)
    return back_substitution(U, y)

def plot_solution(x):
    """
    Plots the solution vector x as a bar chart.

    Parameters:
        x (list of float): Solution vector.
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
    Prompts the user to input matrix A and vector b from the console.

    Returns:
        tuple: (matrix A, vector b)

    Raises:
        ValueError: If input format is incorrect or inconsistent.
    """
    n = int(input("Enter number of variables (n): "))
    A = []
    for i in range(n):
        row_input = input(f"Enter row {i + 1} (space-separated): ")
        row = [float(val) for val in row_input.strip().split()]
        if len(row) != n:
            raise ValueError(f"Row {i + 1} must have exactly {n} values.")
        A.append(row)

    b_input = input("Enter RHS vector b (space-separated): ")
    b = [float(val) for val in b_input.strip().split()]
    if len(b) != n:
        raise ValueError("Vector b length must match number of variables.")

    return A, b
"""
def main():
    """
"""
    Main function: receives matrix and vector from user,
    solves the system using Gaussian Elimination,
    and optionally displays the result as a bar chart.
    """
"""
    try:
        print("Gaussian Elimination Solver")
        A, b = get_matrix_input()
        x = gaussian_elimination(A, b)

        print("\nSolution vector x:")
        for i, val in enumerate(x):
            print(f"x[{i}] = {val:.4f}")

        plot = input("\nShow bar chart of solution? (y/n): ").lower()
        if plot == 'y':
            plot_solution(x)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
"""
