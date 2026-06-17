import numpy as np 

# aggregate functions are used to perform operations on arrays and return a single value.
# some common aggregate functions are: sum, mean, min, max, std, var, etc.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(np.sum(arr))  # sum of all elements
print(np.mean(arr))  # mean of all elements
print(np.min(arr))  # minimum value
print(np.max(arr))  # maximum value
print(np.std(arr))  # standard deviation
print(np.var(arr))  # variance
print(np.argmax(arr))  # index of maximum value
print(np.argmin(arr))  # index of minimum value
print(np.sum(arr, axis=0))  # sum of each column
print(np.sum(arr, axis=1))  # sum of each row
