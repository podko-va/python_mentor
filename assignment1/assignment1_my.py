# Write your code here.
def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

def calc(num1, num2, operation="multiply"):
    try:        
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "int_divide":
            return num1 // num2
        elif operation == "power":
            return num1 ** num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)   
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

def grade(*args):
    try:
        res = sum(args)/len(args)
        return "A" if res>=90 else "B" if res>=80 else "C" if res>=60 else "F" 
    except: return f"Invalid data was provided." 
    
def repeat(st,count):
    res = ""
    for i in range(count):
        res+=st
    return res

def student_scores(method, **kwargs):
    if method == "mean":
        return sum(kwargs.values())/len(kwargs)
    else:
        return max(kwargs, key = kwargs.get)
    
def titleize(st: str):
    return " ".join(i if i in ["a", "on", "an", "the", "of", "and", "is", "in"] and j!=0 and j!=len(st.split())-1 else i.capitalize() for j,i in enumerate(st.split()))

def hangman(secret,guess):
    res = ""
    for i in list(secret):
        if i in guess:
            res+=i
        else: res+="_"
    return res

def pig_latin(stri):
    res = ""
    for st in stri.split(" "):
        if st[0] in "aeiou":
            res+= st+"ay"
        elif st[0:2] == "qu":
            res+= st[2:]+"quay"
        else: 
            i = 0
            while(st[i] not in "aeiou"):
                i+=1
            if st[i-1:i+1] == "qu":
                res+= st[i+1:]+st[:i+1]+"ay"
            else:
                res+= st[i:]+st[:i]+"ay"
        res+=" "
    return res[:-1]

print(pig_latin("the quick brown fox"))