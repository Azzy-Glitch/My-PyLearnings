import pandas as pd

# df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv') # Read a CSV file from the specified path and create a DataFrame
df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv', index_col='Name') # Read the CSV file and set the first column as the index of the DataFrame

# Aggregation = Performing a calculation on a group of data to get a single value that summarizes the group

print(df.mean(numeric_only=True))  # Calculate and print the mean of each numeric column in the DataFrame
print(df['Height'].mean())  # Calculate and print the mean of the 'Height' column in the DataFrame
print(df['Weight'].mean())  # Calculate and print the mean of the 'Weight' column in the DataFrame

print(df.sum(numeric_only=True))  # Calculate and print the sum of each numeric column in the DataFrame
print(df['Height'].sum())  # Calculate and print the sum of the 'Height'
print(df['Weight'].sum())  # Calculate and print the sum of the 'Weight' column in the DataFrame

print(df.min(numeric_only=True))  # Calculate and print the minimum value of each numeric column in the DataFrame
print(df['Height'].min())  # Calculate and print the minimum value of the 'Height
print(df['Weight'].min())  # Calculate and print the minimum value of the 'Weight' column in the DataFrame

print(df.max(numeric_only=True))  # Calculate and print the maximum value of each numeric column in the DataFrame
print(df['Height'].max())  # Calculate and print the maximum value of the 'Height' column in the DataFrame
print(df['Weight'].max())  # Calculate and print the maximum value of the 'Weight' column in the DataFrame

print(df.count())  # Calculate and print the count of non-null values in each column of the DataFrame
print(df['Height'].count())  # Calculate and print the count of non-null values in
print(df['Weight'].count())  # Calculate and print the count of non-null values in the 'Weight' column of the DataFrame

group = df.groupby('Type 1')  # Group the DataFrame by the 'Type 1' column
print(group['Height'].mean())  # Calculate and print the mean of the 'Height'
print(group['Weight'].mean())  # Calculate and print the mean of the 'Weight' column for each group in the DataFrame

