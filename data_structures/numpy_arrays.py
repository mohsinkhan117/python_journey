'''
NumPy stands for Numerical Python and is used for handling large, multi-dimensional arrays and matrices. 
Unlike Python's built-in lists NumPy arrays provide efficient storage and faster
 processing for numerical and scientific computations. It offers functions for linear algebra
 and random number generation making it important for data science and machine learning.
'''


#types of arrays
# 1. one dimensional arrays
# import numpy_arrays as np

import numpy as np
# one dimensional array
a = [1, 2, 3, 4]

arr = np.array(a)

print("List in python : ", a)

print("Numpy Array in python :",
      arr)



# multi dimensional array
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

sample_array = np.array([list_1, 
                         list_2,
                         list_3])
print("Numpy multi dimensional array in python\n",
      sample_array)


print(type(list_1))

print(type(sample_array))