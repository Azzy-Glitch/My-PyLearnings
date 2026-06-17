import numpy as np

# broadcasting allows numpy to perform operations on arrays of different shapes and sizes.
# it automatically expands the smaller array to match the shape of the larger array.

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]])
arr2 = np.array([[1, 2, 3]])  # shape (1, 3)

print(arr1.shape)  # (4, 3)
print(arr2.shape)  # (1, 3)

print(arr1 * arr2)