import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
                [17, 18, 19, 20]])

#array slicing
# arr[rows, columns]
#arr[start:stop:step, start:stop:step]

print(arr[1:4])  # Print the rows from index 1 to 3 (inclusive of index 1 and exclusive of index 4)

# column_slice = arr[:, 1:3]  # Create a slice of the array that includes all rows and columns from index 1 to 2
# print(column_slice)  # Print the sliced array that includes the specified columns

# row_slice = arr[1:4, :]  # Create a slice of the array that includes rows from index 1 to 3 and all columns
# print(row_slice)  # Print the sliced array that includes the specified rows and all columns