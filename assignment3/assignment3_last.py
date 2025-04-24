import pandas as pd


#Task 1

task1_dict = {
       'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(task1_dict)

print(task1_data_frame)

# create a copy
task1_with_salary = task1_data_frame.copy()

#add a column
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)


#increment the age
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print (task1_older)

#save to CSV
task1_older.to_csv("employees.csv", index=False)


#Task 2

import json

task2_employees = pd.read_csv("employees.csv")
print (task2_employees)


additional_employees = {
    "Name": ["Eve", "Frank"],
    "Age": [28, 40],
    "City": ["Miami", "Seattle"],
    "Salary": [60000, 95000]
}

with open('additional_employees.json', 'w') as f:
    json.dump(additional_employees, f)

json_employees = pd.read_json('additional_employees.json')
print (json_employees)

#combines JSON and CSV

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


# Task 3

first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print (employee_shape)

more_employees.info()


#Task 4

dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()
print(clean_data)

# clean_data.drop_duplicates(inplace= True)
clean_data = clean_data.drop_duplicates()
print (clean_data)

#Cleaning Age 

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print (clean_data)

#Cleaning Salary

clean_data['Salary'] = clean_data['Salary'].replace(["unknown", "n/a"], pd.NA) #pd.NA = NAN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print (clean_data)


clean_data['Age'] = pd.to_numeric(clean_data['Age'].fillna(clean_data['Age'].mean()))
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'].fillna(clean_data['Salary'].median()))
print(clean_data)

# #converting Hire Date

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce")
print(clean_data)

# #Text Standardization

clean_data["Name"] = clean_data['Name'].str.strip().str.upper()
clean_data["Department"] = clean_data['Department'].str.strip().str.upper()
print(clean_data)