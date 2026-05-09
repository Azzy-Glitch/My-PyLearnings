import pandas as pd

# df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv') # Read a CSV file from the specified path and create a DataFrame
df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv', index_col='Name') # Read the CSV file and set the first column as the index of the DataFrame

# print(df.head()) # Print the first 5 rows of the DataFrame to get an overview of the data

# print(df.to_string())  # Print the entire DataFrame as a string to see all rows and columns without truncation

#Selection by column
# print(df['Name'])  # Print the 'Name' column of the DataFrame
# print(df.Name)  # Print the 'Name' column of the DataFrame using attribute access
# print(df[['Name', 'Height']])  # Print the 'Name' and 'Height' columns of the DataFrame

#Selection by row
# print(df.loc[0])  # Print the first row of the DataFrame using label-based indexing
# print(df.iloc[0])  # Print the first row of the DataFrame using integer-based indexing
# print(df.loc['Pikachu'])  # Print the row for 'Alice' using label-based indexing
# print(df.loc['Charizard'], ['Height, Weight'])  # Print the row for 'Charizard' using label-based indexing
# print(df.loc['Charizard':'Pikachu', ['Height', 'Weight']])  # Print the 'Height' and 'Weight' for 'Charizard' using label-based indexing
# print(df.iloc[0:11]) # Print the first 11 rows of the DataFrame using integer-based indexing
# print(df.iloc[0:11:2, 0:2]) # Print every second row from the first 11 rows and the first two columns of the DataFrame using integer-based indexing
