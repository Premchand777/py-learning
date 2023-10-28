################# NumPy ####################

# numpy is a numerical python module
# numpy is a fundamental package for `scientific computing`
# numpy is a popular computational and `machine learning library`
# numpy is an `advanced array-processing package`
# high performance multi-dimensional array object
# efficient multi-dimensional container of generic data

'''
NumPy Provides An array object of arbitrary homogeneous items.
Fast mathematical operations over arrays.
Linear Algebra, Fourier Transforms, Random Number Generation.
'''

# Arrays in numpy
'''
Array in numpy is a table of elements (usually numbers).
Array must be of same data type, but can have different data types.
indexed by a tuple of positive integers.
in numpy, no of dimensions of the array is called `rank` of the array.
an Array class in numpy is called as `ndarray`.
'''

import numpy as np

nums = np.array([1, 2, 3, 4, 5, 0])
print(nums, type(nums)) # [1 2 3 4 5 0], <class 'numpy.ndarray'>
print(nums[0], nums[::-1]) # 1, [0 5 4 3 2 1]
print(nums.mean(), nums.min(), nums.all(), nums.any(), nums.sum(), '\n') # 2.5, 0, False, True, 15

strs = np.array(['Hi','Hello'])
print(strs) # ['Hi', 'Hello']

fl = np.array([1.2, 5, 'Hi','Hello', 1])
print(fl) # ['1.2' '5' 'Hi' 'Hello' '1'] -> due to upcasting

# Array attributes
'''
numpy uses the class ndarray for arrays.
ndarray object contains data stored in arrays and attributes
'''

# shape - returns tuple indicating rows and columns
nums = np.array([[1,2,6],[3,4,5]])
print(nums.shape) # (2, 3) means 2 rows and 3 columns

mda = np.array([
    [1, 2, 3], [3, 4, 4], [5, 6, 3]
])

print(mda, mda.shape) # [[1, 2, 3], [3, 4, 4], [5, 6, 3]], (3, 3) 3 rows and 3 columns

# mda = np.array([
#     [1, 2, 0], [3, 4, 5, 9] # raises ValueError because of inhomogeneous length of arrays
# ])
# print(mda.shape)

# ndim -> no of dimensions
print(nums.ndim, mda.ndim) # 2, 2

# size -> number of elements
print(nums.size, mda.size) # 6, 9

# nbytes -> tells how big our array is(occupied memory in bytes) - returns the number of bytes
print(nums.nbytes, strs.nbytes, strs.shape) # 48, 40, (2,)

print((np.array([[1, 2, 3], [3, 4, 5]])).shape) # (2, 3)

# array data types

# extra chars will be cut out to the below array. U3 means unicode string of max length 3
strs2 = np.array(['Hii', 'Bye', 'Hmmok', 'test', 'mayer'], dtype='<U3') 
print(strs2) # ['Hii' 'Bye' 'Hmm' 'tes' 'may']

# dtype -> data type of an array
print(strs2.dtype) # <U3

# observe difference for below 3
fl = np.array([1, 2, 3, 4.5, 5.6])
print(fl, fl.dtype) # [1.  2.  3.  4.5 5.6] float64

fl = np.array([1, 2, 3, 4.5, 5.6, 7])
print(fl, fl.dtype) # [1.  2.  3.  4.5 5.6 7. ] float64

fl = np.array([1, 2, 3, 4.5, 5.6, 7], dtype=int)
print(fl, fl.dtype) # [1 2 3 4 5 6 7] int64

inte = np.array([123456789, 2, 3, 4], dtype=np.int8)
print(inte, inte.dtype) # [1 2 3 4] int8
print(np.array(123456789).astype(np.int8)) # need to convert out of bound py integers to desired type using this approach
# because automatic conversion in the above context will be deprecated in numpy soon.

