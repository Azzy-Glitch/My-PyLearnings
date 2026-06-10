import pandas as pd  # Import the pandas library for data manipulation and analysis

# iloc is used for integer-based indexing, where you can access elements by their position in the Series or DataFrame. It uses zero-based indexing,
# meaning the first element is accessed with index 0, the second with index 1, and so on.
# loc is used for label-based indexing, where you can access elements by their labels or index names.
# It allows you to access elements using the actual labels of the index,
calories = {'Monday': 2000, 'Tuesday': 2200, 'Wednesday': 2100, 'Thursday': 2300, 'Friday': 2500}  # Define a dictionary with days of the week as keys and calorie intake as values

series = pd.Series(calories)  # Create a pandas Series from the dictionary

print(series)  # Print the Series to see the days and their corresponding calorie intake

print(series['Monday'])  # Print the calorie intake for Monday using label-based indexing

series.iloc[0] += 2100  # Update the calorie intake for Monday to 2100 using integer-based indexing

print(series['Monday'])  # Print the updated calorie intake for Monday

series.loc['Tuesday'] = 2300  # Update the calorie intake for Tuesday to 2300 using label-based indexing

print(series[series > 2200])  # Print the days and their calorie intake where the intake is greater than 2200

print(series[series < 2200])  # Print the days and their calorie intake where the intake is less than 2200

# Output:

# Monday       2000
# Tuesday      2200
# Wednesday    2100
# Thursday     2300
# Friday       2500

# Monday       2000
# Monday       4100

# Tuesday      2300
# Thursday     2300
# Friday       2500

# Wednesday    2100