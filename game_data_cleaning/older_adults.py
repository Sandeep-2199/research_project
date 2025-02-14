import pandas as pd
from tabulate import tabulate

# Read the CSV file
file_path = "/Users/sandeep/Documents/RA Work/Game Data_Older Adults.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(tabulate(data.head(), headers='keys', tablefmt='psql'))
 
# Basic data analysis
print("Summary statistics:")
print(tabulate(data.describe()))

print("\nMissing values:")
print(data.isnull().sum())

print("\nData types:")
print(data.dtypes)

# Example of a simple analysis: count the number of unique values in a column
column_names = ['participantNumber', 'isCongruent', 'reactionTime']  # Replace with your actual column names
for column_name in column_names:
    print(f"\nNumber of unique values in '{column_name}':")
    unique_values = []
    for column_name in column_names:
        unique_values.append([column_name, data[column_name].nunique()])

    print("\nNumber of unique values in each column:")
    print(tabulate(unique_values, headers=["Column Name", "Unique Values"], tablefmt="grid"))