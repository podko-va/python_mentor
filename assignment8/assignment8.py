import sqlite3
# Example using SQLite
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Projects")

cursor.execute("""
               CREATE TABLE Projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);""")
cursor.execute("""
    INSERT INTO Projects (name, department) VALUES
        ('Project A', 'HR'),
        ('Project B', 'IT'),
        ('Project C', 'Finance');
""")
print("All projects:")
query = """
SELECT *
FROM Projects;
"""
cursor.execute(query)


print(cursor.fetchall())

conn.close()