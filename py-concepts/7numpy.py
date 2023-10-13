# numpy
# numpy is a numerical python module
# numpy is a fundamental package for scientific computing
# numpy is a popular computational and machine learning library
# numpy is an advanced array-processing package
# high performance multi-dimensional array object
# efficient multi-dimensional container of generic data
'''NumPy
Provides
An array object of arbitrary homogeneous items
Fast mathematical operations over arrays
Linear Algebra, Fourier Transforms, Random Number Generation'''

# Arrays in numpy
'''
Array in numpy is a table of elements (usually numbers).
Array must of same data type.
indexed by a tuple of positive integers.
in numpy, no of dimensions of the array is called rank of the array.
an Array class in numpy is called as ndarray.
'''

import numpy as np

nums = np.array([1, 2, 3, 4, 5, 0])
print(nums, type(nums))
print(nums[0], nums[::-1])
print(nums.mean(), nums.min(), nums.all(), nums.any(), '\n')

strs = np.array(['Hi','Hello'])
print(strs)

fl = np.array([1.2, 5, 'Hi','Hello'])
print(fl) # ['Hi' 'Hello' '1.2' '5']

# Array attributes
'''
numpy uses the class ndarray for arrays.
ndarray object contains data stored in arrays and attributes
'''

# shape - returns tuple indicating rows and columns
print(nums.shape)

mda = np.array([
    [1, 2, 3], [3, 4, 4], [5, 6, 3]
])

print(mda, mda.shape)

# mda = np.array([
#     [1, 2, 0], [3, 4, 5, 9] # raises ValueError because of inhomogeneous length of arrays
# ])
# print(mda.shape)

# ndim -> no of dimensions
print(nums.ndim, mda.ndim)

# size -> number of elements
print(nums.size, mda.size)

# dtype -> data type of an array
print(nums.dtype, strs.dtype)
# extra chars will be cut out to the below array. U3 means unicode string of max length 3
strs2 = np.array(['Hii', 'Bye', 'Hmmok'], dtype='<U3') 
print(strs2, strs2.dtype)

# nbytes -> tells how big our array is(occupied memory in bytes) - returns the number of bytes
print(nums.nbytes, strs.nbytes, strs2.nbytes)

