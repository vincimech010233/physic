import numpy as np
from scipy.linalg import lu, solve_triangular

def gaussian_Elim(A, v):
    '''
    Solves the system of equations associated with the matrix A and vector v
    using Gaussian Elimination.
    :param A: square matrix
    :param v: vector
    :return: vector containing the solutions to the system of equations
    '''
    N = len(v)
    # Gaussian Elimination
    for m in range(N):
        # Partial pivoting
        largest = abs(A[m, m])
        largest_row = m
        for i in range(m + 1, N):
            if abs(A[i, m]) > largest:
                largest = abs(A[i, m])
                largest_row = i
        if largest_row != m:
            # Switch rows in A
            current_row = np.copy(A[m, :])  # Need to use copy because A[m, :] is a reference
            A[m, :] = A[largest_row, :]
            A[largest_row, :] = current_row

            # Switch rows in v
            v[m], v[largest_row] = v[largest_row], v[m]

        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i, :] -= mult * A[m, :]
            v[i] -= mult * v[m]

    # Back substitution
    x = np.empty(N, float)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i] * x[i]

    return x

def jacobi(A, b, tolerance=1e-10, max_iterations=100):
    '''
    Solves the system of equations using the Jacobi iterative method.
    :param A: square matrix
    :param b: vector
    :param tolerance: stopping criterion for the solution
    :param max_iterations: maximum number of iterations
    :return: vector containing the solutions to the system of equations
    '''
    x = np.zeros_like(b, dtype=float)
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(A.shape[0]):
            s = sum(A[i, j] * x[j] for j in range(A.shape[1]) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            break
        x = x_new
    return x


# Matrices and vectors for testing
A = np.array([[4, -1, -1, -1],
              [1, -2, 0, 1],
              [-1, 0, 3, -1],
              [1, 1, 1, -4]], float)
v = np.array([5, 0, 5, 0], float)

B = np.array([[0, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)
w = np.array([-4, 3, 9, 7], float)

# Gaussian Elimination
print("Gaussian Elimination:")
print(gaussian_Elim(A.copy(), v.copy()))
print(gaussian_Elim(B.copy(), w.copy()))

# Using numpy.linalg.solve
print("\nUsing numpy.linalg.solve:")
print(np.linalg.solve(A, v))
print(np.linalg.solve(B, w))

# Using LU decomposition
print("\nUsing LU decomposition:")
P, L, U = lu(A)
y = solve_triangular(L, np.dot(P, v), lower=True)
x = solve_triangular(U, y)
print(x)

P, L, U = lu(B)
y = solve_triangular(L, np.dot(P, w), lower=True)
x = solve_triangular(U, y)
print(x)

# Using Jacobi method
print("\nUsing Jacobi method:")
print(jacobi(A, v))
print(jacobi(B, w))

# Using matrix inversion (not recommended)
print("\nUsing matrix inversion:")
print(np.dot(np.linalg.inv(A), v))
print(np.dot(np.linalg.inv(B), w))
