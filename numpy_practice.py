

import numpy as np

# print(np.random.randn(2,3))

# print(np.random.randint(2,10))

# print(np.random.choice([1,2,3,4]))

# print(np.linspace(-10,10,50))

# print(np.identity(3))

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(a.shape)
# shape=a.reshape(2,3)
# print(shape)

print(a)

# print(a.size)
# print(a.itemsize)
# print(a.astype(np.int32))
# print(a.dtype)

print(a[::2,1::2])