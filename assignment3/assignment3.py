import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
task1_data_frame = df

task1_with_salary = task1_data_frame.copy()
task1_with_salary = task1_with_salary.assign(Salary=[70000, 80000, 90000])
# print(task1_with_salary)

# task1_with_salary["Salary1"] = [70000, 80000, 90000]
# print(task1_with_salary)

# data = pd.read_csv("./dirty_data.csv", sep = "|")
# print(data.head())

# increment the age column
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# save to a csv names employees.csv
task1_older.to_csv('employees.csv', index=False)

task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

print(task2_employees.columns)
print(len(task2_employees.columns))
print(task2_employees.shape)

json_employees = pd.read_json('additional_employees.json')

# Print the loaded JSON data
# print(json_employees)

more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)

print(more_employees)

first_three = more_employees.head(3)
print(first_three)
last_two = more_employees.tail(2)
print(last_two)
employee_shape = more_employees.shape
print(employee_shape)
print(more_employees.info())
print(more_employees.describe())
print(more_employees.select_dtypes(include=[np.number]).corr())
num_cols = df.select_dtypes(include=[np.number])
print(num_cols)

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()
print(clean_data)
clean_data.drop_duplicates(inplace=True)

# clean_data["Age"] = clean_data["Age"].astype(int).fillna(df['Age'].mean())
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")


# 4. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].str.strip()

clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"],pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
# 5. Fill missing numeric values (use fillna).  Fill Age which the mean and Salary 
# with the median
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
print(clean_data)
median = clean_data["Salary"].median()
print(median)
clean_data["Salary"] = clean_data["Salary"].fillna(median)
# 6. Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
# 7. Strip extra whitespace and standardize Name and Department as uppercase

clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
clean_data["Age"] = clean_data['Age'].astype(int)

print(clean_data)