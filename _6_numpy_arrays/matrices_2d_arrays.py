import numpy as np

# ============================================================
# NUMPY 2D ARRAYS / MATRICES — QUICK REVISION SHEET
# A 2D array is just a "grid" of numbers: rows and columns.
# Same numpy engine as 1D vectors, but with an extra dimension.
# ============================================================


print("\n================= CREATING 2D ARRAYS (MATRICES) =================")
# A 2D array is created from a list of lists -> each inner list is a row
M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M)
print(type(M))

# Other common ways to build matrices without typing every value
print(np.zeros((2, 3)))     # 2 rows, 3 columns, all zeros -> good placeholder
print(np.ones((3, 2)))      # 3 rows, 2 columns, all ones
print(np.eye(3))            # 3x3 identity matrix (1s on diagonal, 0s elsewhere)
print(np.full((2, 2), 7))   # 2x2 matrix filled entirely with the value 7
print(np.random.randint(0, 10, (2, 3)))   # 2x3 matrix of random ints (0-9)

# -----------------------------------------------------------

print("\n================= MATRIX PROPERTIES =================")
# Same attributes as 1D arrays, but now shape has TWO numbers
print(M.ndim)     # number of dimensions -> 2 for a matrix
print(M.shape)    # (rows, columns) -> (2, 3)
print(M.size)     # total number of elements -> 6
print(M.dtype)    # data type of the elements

# -----------------------------------------------------------

print("\n================= INDEXING (ROW, COLUMN) =================")
# 2D indexing uses M[row, column] - both indices in ONE set of brackets
print(M[0, 0])     # first row, first column -> 1
print(M[1, 2])     # second row, third column -> 6
print(M[-1, -1])   # last row, last column -> 6 (negative indexing works too)

# Accessing an entire row or column
print(M[0])        # entire first row      -> [1 2 3]
print(M[:, 0])      # entire first column   -> [1 4]  (":" means "all rows")

# -----------------------------------------------------------

print("\n================= SLICING A MATRIX =================")
# M[row_start:row_end, col_start:col_end] -> slice both dimensions at once
print(M[:, 1:3])     # all rows, columns 1 to 2       -> [[2 3] [5 6]]
print(M[0:1, :])     # first row only, all columns     -> [[1 2 3]]
print(M[:, :2])      # all rows, first 2 columns       -> [[1 2] [4 5]]

# -----------------------------------------------------------

print("\n================= MATRIX ARITHMETIC (ELEMENT-WISE) =================")
# Same rule as 1D arrays: +, -, *, / all work ELEMENT BY ELEMENT automatically
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)     # element-wise addition       -> [[6 8] [10 12]]
print(A - B)     # element-wise subtraction    -> [[-4 -4] [-4 -4]]
print(A * B)     # element-wise multiplication -> [[5 12] [21 32]]  (NOT matrix multiplication!)
print(A / B)     # element-wise division

# -----------------------------------------------------------

print("\n================= SCALAR BROADCASTING =================")
# A single number applies to every element automatically
print(A + 10)    # adds 10 to every element
print(A * 2)     # doubles every element

# -----------------------------------------------------------

print("\n================= MATRIX MULTIPLICATION (TRUE DOT PRODUCT) =================")
# IMPORTANT: A * B above is element-wise, NOT real matrix multiplication.
# True matrix multiplication needs @ or np.dot() / np.matmul()
print(A @ B)              # method 1 -> real matrix multiplication
print(np.dot(A, B))       # method 2 -> same result as @
print(np.matmul(A, B))    # method 3 -> same result again

# Rule: for A(m x n) @ B(n x p), the inner dimensions (n) must match,
# result shape is (m x p)

# -----------------------------------------------------------

print("\n================= TRANSPOSE =================")
# Transpose -> flips rows into columns and columns into rows
print(M)
print(M.T)          # method 1 -> shorthand attribute
print(M.transpose()) # method 2 -> same result as .T
print(M.shape, "->", M.T.shape)   # shape flips from (2,3) to (3,2)

# -----------------------------------------------------------

print("\n================= RESHAPE =================")
# reshape() -> changes the shape WITHOUT changing the data (total size must match)
flat = np.array([1, 2, 3, 4, 5, 6])
print(flat.reshape(2, 3))    # turn a 1D array into a 2x3 matrix
print(flat.reshape(3, 2))    # or a 3x2 matrix - same 6 values, different layout
print(M.reshape(-1))          # -1 means "flatten to 1D automatically" -> [1 2 3 4 5 6]
print(M.flatten())             # same flattening effect, a dedicated method

# -----------------------------------------------------------

print("\n================= STACKING / COMBINING MATRICES =================")
# Joining matrices together along rows or columns
print(np.vstack([A, B]))       # stack vertically (adds rows)    -> shape (4, 2)
print(np.hstack([A, B]))       # stack horizontally (adds columns) -> shape (2, 4)
print(np.concatenate([A, B], axis=0))   # same as vstack -> axis=0 means "along rows"
print(np.concatenate([A, B], axis=1))   # same as hstack -> axis=1 means "along columns"

# -----------------------------------------------------------

print("\n================= AGGREGATE FUNCTIONS WITH axis= =================")
# Without axis, aggregate functions collapse the WHOLE matrix into one value.
# With axis=0 -> operate DOWN each column. With axis=1 -> operate ACROSS each row.
data = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(data.sum())          # sum of ALL elements -> 21
print(data.sum(axis=0))    # sum of each COLUMN   -> [5 7 9]
print(data.sum(axis=1))    # sum of each ROW       -> [6 15]

print(data.mean(axis=0))   # average of each column -> [2.5 3.5 4.5]
print(data.max(axis=1))    # max value in each row    -> [3 6]
print(data.min(axis=0))    # min value in each column -> [1 2 3]

# -----------------------------------------------------------

print("\n================= DETERMINANT / INVERSE (LINEAR ALGEBRA) =================")
# numpy.linalg -> dedicated module for matrix-specific math operations
square = np.array([[4, 7], [2, 6]])

print(np.linalg.det(square))    # determinant -> a single number describing the matrix
print(np.linalg.inv(square))    # inverse matrix -> square @ inverse = identity matrix
print(square @ np.linalg.inv(square))   # proof -> ~identity matrix (rounding may show tiny decimals)

# -----------------------------------------------------------

print("\n================= COPY vs VIEW (ALIASING AWARENESS) =================")
# Just like 1D arrays, slicing a matrix can create a VIEW (shared memory),
# not a full copy - modifying a slice can silently affect the original.
original = np.array([[1, 2], [3, 4]])
view = original[:, :]        # this is a VIEW, not an independent copy
view[0, 0] = 99
print(original)               # original also changed! -> [[99 2] [3 4]]

safe_copy = original.copy()   # .copy() -> TRUE independent copy, like with lists
safe_copy[0, 0] = 1
print(original)               # original stays unaffected this time

# -----------------------------------------------------------

print("\n================= QUICK CHEAT SHEET =================")
#   OPERATION                  1D ARRAY (VECTOR)         2D ARRAY (MATRIX)
#   --------------------------  ------------------------  --------------------------------
#   Shape                        (n,)                        (rows, cols)
#   Indexing                      a[i]                        M[row, col]
#   Element-wise math              +, -, *, /                    +, -, *, /  (same rule)
#   True dot/matrix product          np.dot(u, v) -> scalar          A @ B -> new matrix
#   Aggregate (sum/mean/max...)       collapses to 1 value              use axis=0 (cols) / axis=1 (rows)
#   Reshape                           .reshape(...)                       .reshape(rows, cols)
#   Transpose                          not meaningful for 1D                M.T flips rows/columns