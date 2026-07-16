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


# Shape: Number of elements along with each axis and is returned as a tuple
sample_array = np.array([[0, 4, 2],
                       [3, 4, 5],
                       [23, 4, 5],
                       [2, 34, 5],
                       [5, 6, 7]])

print("shape of the array :",
      sample_array.shape)  # shape of the array : (5, 3)


#  Data type objects (dtype): Data type objects (dtype) is an example of numpy.dtype class.
#  It describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
sample_array_1 = np.array([[0, 4, 2]])

sample_array_2 = np.array([0.2, 0.4, 2.4])

print("Data type of the array 1 :",
      sample_array_1.dtype)   #Data type of the array 1 : int64

print("Data type of array 2 :",
      sample_array_2.dtype) #Data type of array 2 : float64


# Different ways of creating arrays
#1. numpy.array(): Numpy array object in Numpy is called ndarray.
#  We can create ndarray using this function.
# Syntax: numpy.array(parameter)



arr = np.array([3,4,5,5])

print("Array :",arr)

#2. numpy.fromiter(): The fromiter() function create a new one-dimensional array 
# from an iterable object.

#Syntax: numpy.fromiter(iterable, dtype, count=-1)

hello="Hello world"
arr= np.fromiter(hello,dtype='U2')
'''what is dtype:
int32 → integers
float64 → decimal numbers
bool → True/False
U → Unicode strings
Unlike np.array(), the fromiter() function cannot guess the data type automatically because:

It reads elements one-by-one from an iterator
It doesn’t know the full dataset in advance
So it needs explicit instruction on how to store each item'''

#3. numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values 
# within a given interval.

# Syntax:  numpy.arange( start , stop, step , dtype=None )

np.arange(1, 20 , 2, 
          dtype = np.float32)  #array([ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19.], dtype=float32) 



#4. numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. 

# Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

np.linspace(3.5, 10, 3, 
            dtype = np.int32)  #array([ 3,  6, 10], dtype=int32)


# 5. numpy.empty(): This function create a new array of given shape and type without initializing value.

# Syntax: numpy.empty(shape, dtype=float, order='C')

print(np.empty([4, 3],
         dtype = np.int32,
         order = 'f')
)


# 6. numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1).

# Syntax: numpy.ones(shape, dtype=None, order='C')

np.ones([4, 3],
        dtype = np.int32,
        order = 'f')


# 7. numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0). 

# Syntax: numpy.zeros(shape, dtype=None, order='C')

np.zeros([4, 3],
        dtype = np.int32,
        order = 'f')