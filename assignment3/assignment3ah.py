import numpy as np
import pandas as pd


data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Replace placeholders with NaN and convert to numeric
df["Height"] = df["Height"].replace("unknown", pd.NA)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

print("\nAfter conversion to numeric:")
print(df)

# Assignment Tasks 
# Task 1

# Creating DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print("Task 1 - Original DataFrame:")
print(task1_data_frame)

# Adding Salary column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\nTask 1 - With Salary:")
print(task1_with_salary)

# Updating Age column
# Incrementing Age by 1
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\nTask 1 - Age Incremented:")
print(task1_older)

# Saving as CSV
task1_older.to_csv('employees.csv', index=False)



# Task 2: Load from CSV and JSON
# Reading from CSV
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2 - Read from CSV:")
print(task2_employees)

# Create and read from JSON
json_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
json_df = pd.DataFrame(json_data)
json_df.to_json('additional_employees.json', orient='records', lines=False)

json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 - Read from JSON:")
print(json_employees)

# Combining both DataFrames CSV and JSON using concat
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined DataFrame:")
print(more_employees)

# Task 3: Data Inspection
first_three = more_employees.head(3) # using .head(by default 5) 
print("\nTask 3 - First Three Rows:")
print(first_three)

last_two = more_employees.tail(2)
print("\nTask 3 - Last Two Rows:") # using .tail(by default 5)
print(last_two)

#.shape of DataFrame
employee_shape = more_employees.shape
print("\nTask 3 - Shape:")
print(employee_shape)

more_employees.info() # .info() gives a concise summary of the DataFrame

# Task 4: Data Cleaning
# Creating an uncleaned_data.csv to simulate this task
uncleaned_data_content = {
    'Name': [' Alice ', 'Bob', 'Charlie', 'Bob'],
    'Age': ['25', '30', None, '30'],
    'Salary': ['70000', 'unknown', '90000', 'unknown'],
    'Department': [' HR ', 'Engineering', 'Finance', 'Engineering'],
    'Hire Date': ['2020-01-15', 'not available', '2018-06-23', 'not available']
}
uncleaned_data_df = pd.DataFrame(uncleaned_data_content)
uncleaned_data_df.to_csv('uncleaned_data.csv', index=False)

# Load unclean data
uncleaned_data = pd.read_csv('uncleaned_data.csv')
print("\nTask 4 - Uncleaned Data:")
print(uncleaned_data)


clean_data = uncleaned_data.copy()

# Removing duplicates
clean_data = clean_data.drop_duplicates()
print("\nTask 4 - After Removing Duplicates:")
print(clean_data)

# Converting age to numeric and replacing non-numeric with NaN
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nTask 4 - After Converting Age to Numeric:")
print(clean_data)

#Converting Salary to numeric and replace unknowns with NaN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'].replace(['unknown', 'n/a'], np.nan), errors='coerce')
print("\nTask 4 - After Cleaning Salary:")
print(clean_data)

# Filling missing numeric values
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nTask 4 - After Filling Missing Values:")
print(clean_data)

# Converting Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nTask 4 - After Converting Hire Date:")
print(clean_data)

# White space removal and uppercasing
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nTask 4 - Final Cleaned Data:")
print(clean_data)