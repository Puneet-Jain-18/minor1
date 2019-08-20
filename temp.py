import numpy as np
arr = np.array([[1,4,2],[2,3,4]])

arr2 = np.array([[1,4,6],[2,3,0]])
print(arr.size)
print(arr.ndim)
print(arr.dtype)
print(arr.shape)
arr=np.sort(arr)
print(arr*arr2)
print("00000000000000")
print(arr.cumsum(axis=1))
