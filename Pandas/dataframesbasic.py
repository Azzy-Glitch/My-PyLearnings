import pandas as pd  # Import the pandas library for data manipulation and analysis

data = {"Names": ["Alice", "Bob", "Charlie", "David", "Eve"],  # Define a dictionary with names}
        "Ages": [25, 30, 35, 40, 45],  # Define a list of ages
        "Cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]}  # Define a list of cities

df = pd.DataFrame(data, index=["Employee #1", "Employee #2", "Employee #3", "Employee #4", "Employee #5"])  # Create a pandas DataFrame from the dictionary

# print(df.loc["Employee #1"])  # Print the row for Employee #1 using label-based indexing

# print(df.iloc[0])  # Print the row for Employee #1 using integer-based indexing

# print(df)  # Print the DataFrame to see the structured data

# Add a new column for salaries
df["Salaries"] = [50000, 60000, 70000, 80000, 90000]  # Add a new column to the DataFrame with salary data

# print(df)  # Print the updated DataFrame with the new Salaries column

# Add a new column as jobs
df["Jobs"] = ["Engineer", "Doctor", "Artist", "Lawyer", "Teacher"]  # Add a new column to the DataFrame with job titles

# print(df)  # Print the updated DataFrame with the new Jobs column

# Add a new row for a new employee
new_employee = pd.DataFrame([{"Names": "Frank", "Ages": 50, "Cities": "San Francisco", "Salaries": 100000, "Jobs": "Manager"}], index=["Employee #6"])  # Define a new DataFrame for the employee

df = pd.concat([df, new_employee])  # Concatenate the new employee DataFrame with the existing DataFrame to add the new row

print(df)  # Print the updated DataFrame with the new employee added


