import numpy as np

# filtering allows us to select specific elements from an array based on a condition.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# filter out even numbers
even_numbers = arr[arr % 2 == 0]
print(even_numbers)  # [ 2  4  6  8 10]

# filter out numbers greater than 5
greater_than_five = arr[arr > 5]
print(greater_than_five)  # [ 6  7  8  9 10]

ages = np.array([[18, 22, 15, 30, 25, 17, 19],
                 [20, 21, 16, 28, 24, 18, 17]])

# filter out ages that are greater than or equal to 18
adults = ages[ages >= 18]
print(adults)  # [18 22 30 25 19]

# filter out ages that are less than 18
minors = ages[ages < 18]
print(minors)  # [15 17]

# np.where() function can also be used for filtering. 
# It returns the indices of elements that satisfy a given condition.
indices = np.where(ages > 25, ages, -1)  # returns the ages that are greater than 25, otherwise returns -1
print(indices)  # (array([5, 6, 7, 8, 9]), array([0, 0, 0, 0, 0]))