import sqlite3   # For SQL command execution
import os

def task1(db_path):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()     
        query = """
        select o.order_id, sum(p.price*l.quantity) from orders as o join line_items as l on o.order_id = l.order_id join products as p on p.product_id = l.product_id group by o.order_id order by o.order_id limit 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

def task2(db_path):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor() 
        query = """    select a.customer_id as customer_id_avg, a.customer_name, avg(a.order_sum) 
        from
        (select c.customer_id, c.customer_name, o.order_id, sum(p.price*l.quantity) as order_sum 
        from orders as o join line_items as l 
        on o.order_id = l.order_id 
        join products as p 
        on p.product_id = l.product_id 
        join customers as c 
        on c.customer_id=o.customer_id 
        group by o.customer_id, c.customer_name, o.order_id 
        order by o.order_id) as a group by a.customer_id;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

def task4(db_path):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()   

        query = """
        select e.employee_id, e.first_name, e.last_name, count(o.order_id) 
        from orders as o join employees as e 
        on o.employee_id = e.employee_id 
        group by e.employee_id ,e.first_name, e.last_name
        having count(o.order_id) > 5
        """
        cursor.execute(query)


        results = cursor.fetchall()
        for row in results:
            print(row)

def add_order(cursor, employee_id, customer_id):
    try:
        cursor.execute("INSERT INTO orders (employee_id, customer_id, date) VALUES (?,?,DATE('now'))", (employee_id, customer_id))
        cursor.execute("SELECT order_id FROM orders WHERE date = DATE('now')")
        
        order_id =  cursor.fetchone()[0]
        print(order_id)
        return order_id
    except sqlite3.IntegrityError:
        print("IntegrityError")
        return 

def enrolled_customer(cursor, customer):
    cursor.execute("SELECT * FROM customers WHERE customer_name = ?", (customer,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        customer_id = results[0][0]
        return customer_id
    else:
        print(f"There was no customer named {customer}.")
        return
    

def enrolled_employee(cursor, employee):
    cursor.execute("SELECT * FROM employees WHERE first_name || ' ' || last_name = ?", (employee,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        employee_id = results[0][0]
        return employee_id
    else:
        print(f"There was no employee named {employee}.")
        return
    
def add_orderline(cursor, order_id, product_id):
    try:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?,?,10)", (order_id, product_id))
    except sqlite3.IntegrityError:
        print("IntegrityError") 
    
# Task3
def task3(db_path):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()

        employee_id = enrolled_employee(cursor, 'Miranda Harris')
        customer_id = enrolled_customer(cursor, 'Perez and Sons')
        # Insert data into order table
        order_id = add_order(cursor, employee_id, customer_id)
        # Insert data into line_items table
        cursor.execute("""SELECT product_id FROM products ORDER BY price desc LIMIT 5""")
        results = cursor.fetchall()
        for row in results:
            # print(row[0])
            add_orderline(cursor, order_id, row[0]) 
        
        cursor.execute("SELECT * FROM line_items WHERE order_id = ?", (order_id,))
        results = cursor.fetchall()
        for row in results:
            print(row)

def main():
    print("version", sqlite3.sqlite_version)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../db/lesson.db")
    print("Find the total price of each of the first 5 orders.", sep='\n')
    task1(db_path)
    print("For each customer, find the average price of their orders.", sep='\n')
    task2(db_path)
    print("creating a new order")
    task3(db_path)
    print("Find all employees associated with more than 5 orders")
    task4(db_path)

if __name__ == "__main__":
    main()