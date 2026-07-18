import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# NUMPY 1D ARRAYS / VECTORS — QUICK REVISION SHEET
# Covers: creation, arithmetic, dot & cross product, universal
# functions, aggregate methods, and a speed comparison against
# plain Python loops/append (the reason numpy exists at all).
# ============================================================


print("\n================= CREATING 1D ARRAYS =================")
# np.array() -> converts a list into a numpy array (a "vector")
a = np.array([1, 2, 3, 4])
print(a)
print(type(a))

# Other common ways to create arrays without typing every value
print(np.arange(0, 10, 2))     # start, stop(exclusive), step -> [0 2 4 6 8]
print(np.linspace(0, 1, 5))    # 5 evenly spaced values between 0 and 1 (inclusive)
print(np.zeros(4))             # array of 4 zeros -> useful as a starting placeholder
print(np.ones(4))              # array of 4 ones

# -----------------------------------------------------------

print("\n================= ARRAY PROPERTIES =================")
# Quick attributes to inspect any array (no parentheses -> these are properties, not methods)
print(a.ndim)      # number of dimensions -> 1 for a vector
print(a.shape)      # (4,) -> 4 elements, 1D
print(a.size)       # total number of elements
print(a.dtype)      # data type of the elements (int64, float64, etc.)

# -----------------------------------------------------------

print("\n================= INDEXING & SLICING (SAME AS LISTS) =================")
# Numpy arrays support the same indexing/slicing syntax as lists
print(a[0])       # first element
print(a[-1])      # last element
print(a[1:3])     # slice -> elements at index 1 and 2

# -----------------------------------------------------------

print("\n================= VECTOR ARITHMETIC (ELEMENT-WISE) =================")
# The BIG difference from lists: math operators work element-by-element
# automatically - no loop needed at all.
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print(u + v)     # addition       -> [5 7 9]
print(u - v)     # subtraction    -> [-3 -3 -3]
print(u * v)     # multiplication -> [4 10 18]  (element-wise, NOT dot product)
print(u / v)     # division       -> [0.25 0.4 0.5]

# -----------------------------------------------------------

print("\n================= SCALAR BROADCASTING =================")
# A single number (scalar) is automatically applied to every element -
# this is called "broadcasting", and lists can't do this at all.
print(u + 10)    # adds 10 to every element -> [11 12 13]
print(u * 2)     # doubles every element    -> [2 4 6]

# -----------------------------------------------------------

print("\n================= DOT PRODUCT =================")
# Dot product -> sum of element-wise products; returns a SINGLE number (scalar)
# Formula: u.v = u1*v1 + u2*v2 + u3*v3 ...
print(np.dot(u, v))    # method 1
print(u.dot(v))        # method 2 (called on the array itself)
print(u @ v)           # method 3 -> the @ operator also means "matrix/dot product"

# -----------------------------------------------------------

print("\n================= CROSS PRODUCT =================")
# Cross product -> returns a VECTOR perpendicular to both inputs (3D vectors)
# Mainly meaningful in 3D physics/geometry contexts (torque, normals, etc.)
print(np.cross(u, v))     # -> array([-3, 6, -3])

# For 2D vectors, cross product returns a single scalar (the "z" component)
# NOTE: newer numpy versions (2.0+) print a DeprecationWarning for 2D cross
# products and prefer 3D vectors - the math/output is still correct either way.
u2d = np.array([1, 2])
v2d = np.array([3, 4])
print(np.cross(u2d, v2d))   # -> scalar: 1*4 - 2*3 = -2

# -----------------------------------------------------------

print("\n================= UNIVERSAL FUNCTIONS (ufuncs) =================")
# Universal functions apply a math operation to EVERY element at once,
# instead of writing a manual loop.
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))     # square root of each element -> [1 2 3 4]
print(np.exp(u))        # e^x for each element
print(np.log(arr))      # natural log of each element
print(np.abs(np.array([-1, -2, 3])))   # absolute value of each element
print(np.sin(np.array([0, np.pi/2])))  # sine of each element (radians)
print(np.round(np.array([1.234, 5.678]), 1))   # round each element to 1 decimal

# -----------------------------------------------------------

print("\n================= AGGREGATE / STATISTICAL METHODS =================")
# These collapse an entire array down into a single summary value
data = np.array([4, 8, 6, 2, 10])

print(data.mean())     # average value
print(data.sum())      # total of all elements
print(data.max())      # largest value
print(data.min())      # smallest value
print(data.std())      # standard deviation (spread of values)
print(data.var())      # variance
print(np.median(data)) # middle value when sorted
print(data.argmax())   # INDEX of the largest value (not the value itself)
print(data.argmin())   # INDEX of the smallest value

# -----------------------------------------------------------

print("\n================= OTHER USEFUL METHODS =================")
print(np.sort(data))          # returns a NEW sorted array (ascending)
print(data.reshape(5, 1))     # reshape into 5 rows x 1 column (must fit same size)
print(data.copy())            # independent copy (like list.copy() - avoids aliasing)
print(np.concatenate([u, v])) # joins two arrays into one, end to end

# -----------------------------------------------------------

print("\n================= NUMPY VECTORS vs PLAIN PYTHON LISTS+LOOPS =================")
# This is the core reason numpy exists: vectorized operations are both
# SHORTER to write and dramatically FASTER than manual loops/append.

n = 1_000_000

# ---- Method 1: plain Python list + loop + append (the "manual" way) ----
list_a = list(range(n))
list_b = list(range(n))

start = time.time()
result_list = []
for i in range(n):
    result_list.append(list_a[i] + list_b[i])   # manual element-wise addition
end = time.time()
print(f"Python loop + append time: {end - start:.5f} seconds")

# ---- Method 2: numpy vectorized addition (the "numpy" way) ----
np_a = np.array(list_a)
np_b = np.array(list_b)

start = time.time()
result_np = np_a + np_b     # entire addition happens in one vectorized step
end = time.time()
print(f"Numpy vectorized time:    {end - start:.5f} seconds")

# Numpy is typically MUCH faster because the loop runs in optimized C code
# internally, instead of Python's slower interpreted loop.

# -----------------------------------------------------------

print("\n================= MEMORY: LIST vs NUMPY ARRAY =================")
# Numpy arrays are also more memory-efficient than lists of the same size,
# since lists store pointers to separate Python int objects, while numpy
# stores raw numbers in one contiguous, fixed-type block.
print("List memory (bytes):", sys.getsizeof(list_a))
print("Numpy array memory (bytes):", np_a.nbytes)

# -----------------------------------------------------------

print("\n================= QUICK COMPARISON TABLE =================")
#   FEATURE                  PYTHON LIST + LOOP/APPEND         NUMPY ARRAY
#   ------------------------  --------------------------------  --------------------------------
#   Element-wise math           needs a manual for-loop             just use +, -, *, /  directly
#   Speed on large data          slow (pure Python interpreter)      fast (runs in optimized C)
#   Memory usage                  higher (stores object pointers)     lower (contiguous fixed-type)
#   Built-in math functions        none (must write manually)          sqrt, exp, log, mean, etc. ready to use
#   Broadcasting (scalar + array)   not supported directly               fully supported


# ============================================================
# VECTOR VISUALIZATION (using matplotlib)
# Plots vectors u, v, and their sum z = u + v as arrows,
# to visually confirm what "vector addition" actually looks like.
# ============================================================

def Plotvec1(u, z, v):
    ax = plt.axes()  # generate the full window axes

    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)  # draw vector u in red
    plt.text(*(u + 0.1), 'u')                                        # label it "u"

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)  # draw vector v in blue
    plt.text(*(v + 0.1), 'v')                                        # label it "v"

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)              # draw resultant vector z
    plt.text(*(z + 0.1), 'z')                                        # label it "z"

    plt.ylim(-2, 2)   # fix y-axis view range
    plt.xlim(-2, 2)   # fix x-axis view range


print("\n================= VISUALIZING VECTOR ADDITION =================")
u_vec = np.array([1, 0])
v_vec = np.array([0, 1])
z_vec = u_vec + v_vec        # z is simply the vector sum of u and v

Plotvec1(u_vec, z_vec, v_vec)
plt.savefig("vector_addition.png")   # saved to a file so it works in any environment
print("Plot saved as vector_addition.png")
# plt.show()   # uncomment this locally if you want an interactive pop-up window instead