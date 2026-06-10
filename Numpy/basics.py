import numpy as np

#print(np.__version__)

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

#print(arr)
#print(arr.ndim)  # Print the number of dimensions of the array
#print(arr.shape)  # Print the shape of the array (number of elements in each dimension)
#print(arr[0])  # Print the first element of the array

# Create a 2D array
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6]])

#print(arr_2d)
#print(arr_2d.ndim)  # Print the number of dimensions of the 2D array
#print(arr_2d.shape)  # Print the shape of the 2D array (number of rows and columns)
#print(arr_2d[0, 0])  # Print the element in the first row and first column of the 2D array

# Create a 3D array
arr_3d = np.array([[[1, 2],[3, 4]],
                   [[5, 6],[7, 8]],
                   [[9, 10],[11, 12]]])

#print(arr_3d)
#print(arr_3d.ndim)  # Print the number of dimensions of the 3D array
#print(arr_3d.shape)  # Print the shape of the 3D array (number of blocks, rows, and columns)
#print(arr_3d[0, 0, 0])  # Print the element in the first block, first row, and first column of the 3D array

number = arr_3d[1, 0, 1] + arr_3d[2, 1, 0]  # Access specific elements from the 3D array and add them together
print(number)  # Print the result of the addition