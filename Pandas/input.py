import pandas as pd

# df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv') # Read a CSV file from the specified path and create a DataFrame
df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv', index_col='Name') # Read the CSV file and set the 'Name' column as the index

pokemon = input("Enter the name of the Pokemon you want to search for: ")  # Prompt the user to enter the name of a Pokemon

try:
    pokemon_data = df.loc[pokemon]  # Attempt to retrieve the data for the specified Pokemon using label-based indexing
    print(pokemon_data)  # Print the retrieved data for the specified Pokemon
except KeyError:  # Handle the case where the specified Pokemon is not found in the DataFrame
    print(f"Sorry, {pokemon} not found in the dataset.")  # Print an error message if the Pokemon is not found