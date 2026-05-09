import pandas as pd

# df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv') # Read a CSV file from the specified path and create a DataFrame
df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv', index_col='Name') # Read the CSV file and set the first column as the index of the DataFrame

# Data Cleaning = Fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset

# Drop irrelevant columns
df = df.drop(columns=["Legendary", "No"])  # Remove the 'Legendary' column from the DataFrame
df = df.drop(columns=['Type 2', 'Generation'], inplace=True)  # Remove the 'Type 2' and 'Generation' columns from the DataFrame

#Handle missing values
df = df.dropna(subset=["Type2"], inplace=True)  # Remove any rows with missing values from the DataFrame
df = df['Height'] = df['Height'].fillna(df['Height'].mean())  # Fill any missing values in the 'Height' column with the mean of that column
df = df['Weight'] = df['Weight'].fillna(df['Weight'].mean())  # Fill any missing values in the 'Weight' column with the mean of that column

# Fix inconsistent data
df['Type 1'] = df['Type 1'].str.capitalize()  # Capitalize the first letter of each value in the 'Type 1' column to ensure consistency
df['Type 1'] = df['Type 1'].replace({'Fire': 'FIRE', 'Water': 'WATER'})  # Replace any inconsistent values in the 'Type 1' column with the correct value

# Fix Data Types
df['Height'] = df['Height'].astype(float)  # Convert the 'Height' column to a float data type
df['Weight'] = df['Weight'].astype(float)  # Convert the 'Weight' column to a float data type

# Remove duplicates
df = df.drop_duplicates()  # Remove any duplicate rows from the DataFrame

print(df.to_string())  # Print the entire cleaned DataFrame as a string to see all rows and columns without truncation
