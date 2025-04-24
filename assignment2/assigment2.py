import traceback


# Task 2


def read_employees():
    import csv
    dict = {}
    rows = []
    
    try: 
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            
            count = 1
          
            for row in reader:
                # print (row)
                if count == 1:
                    dict['fields'] = row
                    # print(row)
                else:
                    rows.append(row) 
                    # print()
                count+=1
            #     (fields, rows1)
                # (rows, row)
                
            dict['rows'] = rows
            return dict
                # print(dict)
                   
            
    except FileNotFoundError:
        print("The file 'employees.csv' was not found.")
        
employees = read_employees()
# print(employees)



#Task 3

def column_index(header):
    print(header)
    return employees["fields"].index(header)


#Task 4

def first_name(row):
    first_name_index = column_index('first_name')
    return employees['rows'][row][first_name_index]

print('First Name: \n', first_name(2))
    

  # Task 5
  
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
      
        matches=list(filter(employee_match, employees["rows"]))
        return matches
   
  
  
  #Task 6
  
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


#Task 7

def sort_by_last_name():
    try:
        employees['rows'].sort(key=lambda row: row[column_index('last_name')])
        return employees['rows']
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}") 
    
#Task 8

def employee_dict(row):
    try: 
        keys = employees['fields']
        return dict(zip(keys[1:], row[1:]))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
        print(employee_dict(employees['rows'][0]))
        
    #Task 9

def all_employees_dict():
    
    try: 
        employee_dict = {}
        for row in employees['rows']:
            id = row[0]
            employee_dict[id] = employee_dict[row]
        return employee_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    

print(all_employees_dict())


    #Task 10
    
import os
def get_this_value():
    return os.getenv('THISVALUE')



    # Task 11

import custom_module

def set_that_secret(secret):
    custom_module.set_secret(secret)
    
set_that_secret('ssshhh')
print(custom_module.secret)




    #Task 12
    
import csv

def read_minutes():
    try:
        dict1 = {}
        dict2 = {}
        rows = []
        
        with open('../csv/minutes1.csv', 'r') as file:
            reader = csv.reader(file)
            first = True
        
            for row in reader:
                if first:
                    dict1['fields'] = row
                    first=False
                else:
                    rows.append(tuple(row))
            dict1["rows"] = rows
        
        with open('../csv/minutes2.csv', 'r') as file:
            reader = csv.reader(file)
            first = True
        
            for row in reader:
                if first:
                    dict1['fields'] = row
                    first=False
                else:
                    rows.append(tuple(row))
            dict2["rows"] = rows
        return dict1, dict2
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    
        
minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)
        
        
        

        
        
        
#     #Task 13
    
def create_minutes_set():
    try:
        return set(minutes1['rows']).union(set(minutes2['rows']))   

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
minutes_set = create_minutes_set()        
print(minutes_set)




#Task 14

from datetime import datetime


def create_minutes_list():
    try:
        minutes_list = list(minutes_set)
        converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
        return converted_list
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
minutes_list= create_minutes_list()
print(minutes_list)








#Task 15

def write_sorted_list():
    try:
        minutes_list.sort(key=lambda x: x[1])
        
        # convert the list
        converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
        
        #write csv
        with open('assignment2/minutes.csv', 'w') as csvwfh:
            writer = csv.writer(csvwfh)
            writer.writerow(minutes1['fields']) #header
            for row in converted_list:
                writer.writerow(row)
                
        return converted_list
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
print(write_sorted_list())  