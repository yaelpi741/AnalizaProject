import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def matrix_vector_mult(matrix, vector):
    """
    Multiplies a matrix by a vector.

    Parameters:
        matrix (list of list of float): The coefficient matrix.
        vector (list of float): The vector to multiply.

    Returns:
        list of float: The resulting vector from Ax.
    """
    result = []
    for row in matrix:
        if len(row) != len(vector):
            raise ValueError("Matrix row and vector length mismatch.")
        value = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(value)
    return result

def vector_subtract(v1, v2):
    """
    Subtracts one vector from another.

    Parameters:
        v1 (list of float): First vector.
        v2 (list of float): Second vector.

    Returns:
        list of float: The result of v1 - v2.
    """
    if len(v1) != len(v2):
        raise ValueError("Vector length mismatch.")
    return [v1[i] - v2[i] for i in range(len(v1))]

def max_norm(vector):
    """
    Computes the maximum norm (infinity norm) of a vector.

    Parameters:
        vector (list of float): Input vector.

    Returns:
        float: The maximum absolute value in the vector.
    """
    return max(abs(v) for v in vector)

def residual_norm_max(A, x, b):
    """
    Computes the residual vector and its max norm.

    Parameters:
        A (list of list of float): Coefficient matrix.
        x (list of float): Approximate solution vector.
        b (list of float): Right-hand side vector.

    Returns:
        tuple: Residual vector and its infinity norm.
    """
    Ax = matrix_vector_mult(A, x)
    r = vector_subtract(b, Ax)
    return r, max_norm(r)

def plot_residual(r):
    """
    Plots the residual vector as a bar chart.

    Parameters:
        r (list of float): Residual vector.
    """
    indices = list(range(len(r)))
    bars = plt.bar(indices, r, color='skyblue', edgecolor='black')
    plt.xlabel("Index")
    plt.ylabel("Residual Value")
    plt.title("Residual Vector r = b - Ax")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height,
                 f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function: gets input from user, computes residual and norm, and plots the residual.
    """
    try:
        n = int(input("Enter the number of variables (n): "))

        # Input matrix A
        print("\nEnter the matrix A row by row (each row should have n space-separated numbers):")
        A = []
        for i in range(n):
            row = input(f"Row {i + 1}: ").strip().split()
            if len(row) != n:
                raise ValueError(f"Each row must have exactly {n} values.")
            A.append([float(val) for val in row])

        # Input vector b
        b_input = input("\nEnter the RHS vector b (space-separated): ").strip().split()
        if len(b_input) != n:
            raise ValueError("Vector b must have n values.")
        b = [float(val) for val in b_input]

        # Input approximate solution x
        x_input = input("\nEnter the approximate solution vector x (space-separated): ").strip().split()
        if len(x_input) != n:
            raise ValueError("Vector x must have n values.")
        x_approx = [float(val) for val in x_input]

        # Compute residual and norm
        residual_vector, error = residual_norm_max(A, x_approx, b)

        # Output results
        print("\nResidual vector r =", residual_vector)
        print("Residual max norm (‖r‖∞):", error)

        # Plot residual
        plot_residual(residual_vector)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
