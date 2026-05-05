import pandas as pd  # Import the pandas library for data manipulation and analysis

data = [100, 200, 300, 400, 500]  # Define a list of numerical data

series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])  # Create a pandas Series with custom indices

print(series.loc['A'])  # Print the value at index 'A' using label-based indexing

series.loc['A']= 150  # Update the value at index 'A' to 150

print(series.loc['A'])  # Print the updated value at index 'A'

print(series.iloc[1])  # Print the value at the second position using integer-based indexing

print(series.iloc[0:3])  # Print the values from the first three positions using slicing

print(series[series > 250])  # Print the values in the Series that are greater than 250

# Output:
# 100
# 150
# 200
# B    200
# C    300
# D    400
# E    500

