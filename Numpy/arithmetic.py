import numpy as np

# Arithmetic operations on NumPy arrays

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Scalar operations
arr = np.array([1, 2, 3, 4])

# Adding a scalar
result_add_scalar = arr + 10
print("Addition with scalar:", result_add_scalar)

# Subtracting a scalar
result_sub_scalar = arr - 5
print("Subtraction with scalar:", result_sub_scalar)

# Multiplying by a scalar
result_mul_scalar = arr * 2
print("Multiplication with scalar:", result_mul_scalar)

# Dividing by a scalar
result_div_scalar = arr / 2
print("Division with scalar:", result_div_scalar)

# Vectorized operations

# Using np.add for element-wise addition
print("Vectorized Addition:", np.add(arr1, arr2))
# Using np.subtract for element-wise subtraction
print("Vectorized Subtraction:", np.subtract(arr1, arr2))
# Using np.multiply for element-wise multiplication
print("Vectorized Multiplication:", np.multiply(arr1, arr2))
# Using np.divide for element-wise division
print("Vectorized Division:", np.divide(arr1, arr2))
# Using np.power for element-wise exponentiation
print("Vectorized Power:", np.power(arr1, 2))
# Using np.sqrt for element-wise square root
print("Vectorized Square Root:", np.sqrt(arr1))
# Using np.mod for element-wise modulus
print("Vectorized Modulus:", np.mod(arr1, 2))

# Element-wise operations

# Element-wise addition
result_add = arr1 + arr2
print("Addition:", result_add)

# Element-wise subtraction
result_sub = arr1 - arr2
print("Subtraction:", result_sub)

# Element-wise multiplication
result_mul = arr1 * arr2
print("Multiplication:", result_mul)

# Element-wise division
result_div = arr1 / arr2
print("Division:", result_div)

# Comparison operations

Score = np.array([85, 90, 78, 92])

print("Scores greater than 80:", Score > 80)

Score[Score < 80] = 0
print("Updated Scores:", Score)