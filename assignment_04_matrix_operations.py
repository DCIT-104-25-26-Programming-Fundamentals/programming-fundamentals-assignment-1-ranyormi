# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        row_values = input(f"Enter row {row_index + 1}: ").split()
        row_numbers = [int(value) for value in row_values]
        matrix.append(row_numbers)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:>5}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = []

    for col_index in range(columns):
        new_row = []
        for row_index in range(rows):
            new_row.append(matrix[row_index][col_index])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    result = []
    for row_index in range(len(matrix_a)):
        new_row = []
        for col_index in range(len(matrix_a[0])):
            new_row.append(matrix_a[row_index][col_index] + matrix_b[row_index][col_index])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return None

    result = []
    for row_index in range(rows_a):
        new_row = []
        for col_index in range(cols_b):
            total = 0
            for inner_index in range(cols_a):
                total += matrix_a[row_index][inner_index] * matrix_b[inner_index][col_index]
            new_row.append(total)
        result.append(new_row)

    return result


def main():
    print("Part A — Transpose a Matrix")
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, columns)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    print("\nPart B — Add Two Matrices")
    rows = int(input("Enter number of rows for matrix A: "))
    columns = int(input("Enter number of columns for matrix A: "))
    print("Enter matrix A:")
    matrix_a = read_matrix(rows, columns)
    print("Enter matrix B:")
    matrix_b = read_matrix(rows, columns)
    print("\nSum of Matrices:")
    display_matrix(add_matrices(matrix_a, matrix_b))

    print("\nPart C — Multiply Two Matrices")
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    print("Enter matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    print("Enter matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)

    result = multiply_matrices(matrix_a, matrix_b)
    if result is None:
        print("Error: Matrix dimensions are incompatible for multiplication.")
    else:
        print("\nProduct of Matrices:")
        display_matrix(result)


if __name__ == "__main__":
    main()

