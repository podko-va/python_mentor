import csv

def read_employees():
    my_dict = {}
    my_list = []
    flag = True
    with open('../csv/employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if flag:
                my_dict["fields"] = row
                flag = False
            else: my_list.append(row)
        my_dict["rows"] = my_list
    return my_dict


def read_employees_Alena():
    rows_list =[]
    dict_employees = {}

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            dict_employees["fields"]= next(reader)
            for row in reader:
                rows_list.append(row)
            dict_employees["rows"] = rows_list
        return dict_employees      
        

    except Exception as e:
        print(f'An error occurred while processing the file: {e}')
        exit()

employees = read_employees_Alena()
