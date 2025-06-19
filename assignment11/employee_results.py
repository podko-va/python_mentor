import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("../python_homework/db/lesson.db")

# Step 2: Write the SQL query to join tables and calculate revenue per employee
query = """
SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id
"""

# Step 3: Execute the query and load results into a Pandas DataFrame
employee_results = pd.read_sql_query(query, conn)

# Step 4: Close the database connection
conn.close()

# Step 5: Create a bar chart using Pandas plotting with Matplotlib backend
plt.figure(figsize=(10, 6))  # Set figure size
plt.bar(employee_results['last_name'], employee_results['revenue'], color='skyblue')  # Bar chart

# Step 6: Add titles and labels
plt.title('Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue')

# Step 7: Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Step 8: Adjust layout to fit everything nicely
plt.tight_layout()

# Step 9: Show the plot
plt.show()
