import sqlite3


def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM Subscribers WHERE subscriber_name = ? and subscriber_address = ?", (name, address)) 
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"{name} with {address} is already in the database.")
            return
        else:
            cursor.execute("INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} with address {address} caused an integrity error.")

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM Publishers WHERE publisher_name = ?", (publisher_name,))
        result = cursor.fetchone()
        if result:
            publisher_id = result[0]
            if publisher_id:
                cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)", (name, publisher_id))
            else:
                    print("Publisher not found!")
        else:
                print("Publisher name not found!")
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscription(cursor, subscriber, magazine, expiration_date):
    cursor.execute("SELECT magazine_id FROM Magazines WHERE magazine_name = ?", (magazine,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There was no magazine named {magazine}.")
        return
    cursor.execute("SELECT subscriber_id FROM Subscribers WHERE subscriber_name = ?", (subscriber,))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"There was no subscriber with name {subscriber}.")
        return
    try: 
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
        print(f"GREAT! Subscriber {subscriber} is enrolled in magazine {magazine} with expiration_date = {expiration_date}.")
    except: print(f"Subscriber {subscriber} is already enrolled in magazine {magazine}.")

# Connect to a new SQLite database
try:
    with sqlite3.connect("../db/magazines.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
        print("Database created and connected successfully.")
    
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL UNIQUE,
        subscriber_address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscriptions_id INTEGER PRIMARY KEY,
        magazine_id INTEGER,
        subscriber_id INTEGER,
        expiration_date TEXT  NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
    """)

    print("Tables created successfully.")

    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()
    print("ON for foreign keys")

    # Add publishers
    add_publisher(cursor, "Penguin Books")
    add_publisher(cursor, "National Geographic")
    add_publisher(cursor, "ABC")

    # Add magazines
    add_magazine(cursor, "Science Today", "Penguin Books")
    add_magazine(cursor, "Nature Explorer", "National Geographic")
    add_magazine(cursor, "CCC", "ABC")

    # Add subscribers
    add_subscriber(cursor, "Alice Smith", "123 Main Street")
    add_subscriber(cursor, "Bob Johnson", "456 Oak Avenue")
    add_subscriber(cursor, "Bob Johnson", "456 Oak Avenue")
    add_subscriber(cursor, "Bob", "456 Oak Avenue")

    # Add subscriptions
    add_subscription(cursor, "Alice Smith", "Science Today", "2025-06-01")
    add_subscription(cursor, "Bob Johnson", "Nature Explorer", "2025-12-31")
    add_subscription(cursor, "Bob", "CCC", "2025-12-31")

    # Don't forget to commit your changes
    conn.commit()
    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    for row in result:
        print(row)
    print("a query to retrieve all information from the subscribers table")

    cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
    result = cursor.fetchall()
    for row in result:
        print(row)
    print("a query to retrieve all magazines sorted by name.")

    cursor.execute("SELECT * FROM Publishers")
    result = cursor.fetchall()
    for row in result:
        print(row)
    publisher_name = input("add publisher name from the previous list: ")
    cursor.execute("SELECT Magazines.magazine_name FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.publisher_name ==?", (publisher_name,))
    result = cursor.fetchall()
    for row in result:
        print(*row)
    print("a query to find magazines for a particular publisher")

except sqlite3.Error as e:
    # If there is any SQLite-related error, it will be caught here
    print(f"An error occurred while connecting to the database: {e}")
