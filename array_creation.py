# Create a 1D NumPy array from a Python list [10, 20, 30, 40, 50].

import numpy as np

arr1=np.array([10, 20, 30, 40, 50])

print(type(arr1))

# Create a 1D array of integers from 0 to 9.

arr2=np.arange(0,10)

print(type(arr2))


# Create a 1D array of even numbers from 2 to 20.

arr3=np.arange(2,21,2)
print(arr3)

# Create an array of 10 zeros.

arr4=np.zeros(10)
print(arr4)

# Create an array of 10 ones.

arr5=np.ones(10)
print(arr5)

# Create a 1D array of 10 fives without using a list.

arr6=np.full(10,5)
print(arr6)


# Create an array of integers from 100 to 150 with a step of 10.

arr7=np.arange(100,151,10)
print(arr7)

# Create an array of 10 random integers between 1 and 50.

arr8=np.random.randint(1,50,size=10)
print(arr8)

# Create a 3×3 array with values from 1 to 9.

arr9=np.arange(1,10).reshape(3,3)
print(arr9)

# Create an identity matrix of size 4×4.

arr10=np.identity(4)
print(arr10)