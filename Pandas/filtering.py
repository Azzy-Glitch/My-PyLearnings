import pandas as pd

df = pd.read_csv('D:\\Git Repository\\My-PyLearnings\\Pandas\\data.csv') # Read a CSV file from the specified path and create a DataFrame

# Filtering = Keeping onty the rows that match a certain condition

tall_pokemon = df[df['Height'] >= 2.0]  # Filter the DataFrame to keep only rows where the 'Height' column is greater than 2.0
legendary_pokemon = df[df['Legendary'] == True]  # Filter the DataFrame to keep only rows where the 'Legendary' column is True
water_pokemon = df[(df['Type 1'] == 'Water') | (df['Type 2'] == 'Water')]  # Filter the DataFrame to keep only rows where either 'Type 1' or 'Type 2' column is 'Water'

# print(tall_pokemon)  # Print the filtered DataFrame containing only tall Pokemon
# print(legendary_pokemon)  # Print the filtered DataFrame containing only legendary Pokemon
# print(water_pokemon)  # Print the filtered DataFrame containing only Water-type Pokemon
