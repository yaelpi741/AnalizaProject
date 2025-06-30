import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def matrix_vector_mult(matrix, vector):
    result = []
    for row in matrix:
        if len(row) != len(vector):
            raise ValueError("Matrix row and vector length mismatch.")
        value = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(value)
    return result

def vector_subtract(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vector length mismatch.")
    return [v1[i] - v2[i] for i in range(len(v1))]

def max_norm(vector):
    return max(abs(v) for v in vector)

def residual_norm_max(A, x, b):
    Ax = matrix_vector_mult(A, x)
    r = vector_subtract(b, Ax)
    return r, max_norm(r)

def plot_residual(r):
    indices = list(range(len(r)))
    bars = plt.bar(indices, r, color='skyblue', edgecolor='black')
    plt.xlabel("Index")
    plt.ylabel("Residual Value")
    plt.title("Residual Vector r = b - Ax")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Add value labels on top of bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height,
                 f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()

def main():
    # Define matrix A, RHS vector b, and approximate solution x
    A = [
        [3, 2],
        [1, 4]
    ]
    b = [5, 6]
    x_approx = [1, 1]  # Example approximate solution

    # Calculate residual and max norm
    residual_vector, error = residual_norm_max(A, x_approx, b)

    # Print results
    print("Residual vector r =", residual_vector)
    print("Residual max norm (‖r‖∞):", error)

    # Show graph
    plot_residual(residual_vector)

if __name__ == "__main__":
    main()
