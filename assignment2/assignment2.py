import os
import csv
import custom_module
from datetime import datetime

def diary():
    try:
        file_path = os.path.join(os.getcwd(),'diary.txt')
        print(f'dir = {file_path}')
        with open('diary.txt', 'w') as file:
            new_str = input("What happened today? ")
            while new_str!="done for now":
                file.write(new_str+ "\n")
                new_str = input("What else? ")
    except KeyboardInterrupt:
        print(f"An error occurred writing the file")
    else:
        print("The file was written successfully.")


# print(diary())  

def read_employees():
    my_dist = dict()
    my_list = []

    with open('../csv/employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:            
            my_list.append(row)
    my_dist["fields"] = my_list[0]
    my_dist["rows"] = my_list[1:]
    return my_dist

employees = read_employees()    
# print(employees)

def column_index(employee_id):
    return employees["fields"].index(employee_id)

employee_id_column = column_index("employee_id")
# print(employee_id_column)

def first_name(num_row):
    return employees["rows"][num_row][column_index("first_name")]

# print(first_name(2))

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

# print(employee_find(3)[0])
def employee_find_2(employee_id):
   return list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
  
def sort_by_last_name():
    employees["rows"].sort(key = lambda x : x[column_index("last_name")])
    return employees["rows"]
# print(sort_by_last_name())
def employee_dict(row):
    n_dist = dict()
    for i in range(len(employees["fields"])):
        if employees["fields"][i] != 'employee_id': 
            n_dist[employees["fields"][i]] = row[i]
    return n_dist

# print(employee_dict(employees["rows"][0]))
def  all_employees_dict():
    long_dict = dict()
    for row in employees["rows"]:
        long_dict[row[0]] = employee_dict(row)
    return long_dict
# print(all_employees_dict())

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(par):
    custom_module.set_secret(par)

def read_minutes():
    minute1, minute2 = dict(), dict()
    my_list = []
    with open('../csv/minutes1.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:            
                my_list.append(tuple(row))
            minute1["fields"] = my_list[0]
            minute1["rows"] = my_list[1:]
    my_list = []
    with open('../csv/minutes2.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:            
                my_list.append(tuple(row))
            minute2["fields"] = my_list[0]
            minute2["rows"] = my_list[1:]
    return minute1, minute2

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    my_set = set()
    for row in minutes2["rows"]:
        my_set.add(row)
    for row in minutes1["rows"]:
        my_set.add(row)
    return my_set 

minutes_set = create_minutes_set()   

def create_minutes_list():
    my_list = []
    for row in list(minutes_set):
        my_list.append((row[0], (datetime.strptime(row[1], "%B %d, %Y"))))
    return my_list

minutes_list = create_minutes_list()    

def write_sorted_list():
    my_list = []
    minutes_list.sort(key = lambda row: row[1])
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([minutes1["fields"][0],minutes1["fields"][1]])
        for row in minutes_list:
            writer.writerow((row[0],datetime.strftime(row[1], "%B %d, %Y")))
            my_list.append((row[0],datetime.strftime(row[1], "%B %d, %Y")))
    return my_list
        
write_sorted_list()