import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the database
conn = sqlite3.connect("../python_homework/db/lesson.db")

# Step 2: SQL query to get order_id and total_price (sum of price * quantity per order)
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

# Step 3: Load query result into DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Close the connection
conn.close()

# Step 5: Calculate cumulative revenue using cumsum()
df['cumulative'] = df['total_price'].cumsum()

# Alternative: Using apply (less efficient, just for learning)
# def cumulative(row):
#     totals_above = df['total_price'][0:row.name + 1]
#     return totals_above.sum()
# df['cumulative'] = df.apply(cumulative, axis=1)

# Step 6: Plot cumulative revenue vs order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', linestyle='-', color='green')

# Step 7: Add titles and labels
plt.title('Cumulative Revenue by Order ID')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')

# Step 8: Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
