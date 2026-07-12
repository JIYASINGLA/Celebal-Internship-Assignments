import sqlite3
from datetime import datetime, timedelta

# User Inputs
print("=" * 50)
print("E-Commerce Order Analytics Report")
print("=" * 50)
report_type = input("Enter report type (daily/weekly/monthly): ").strip().lower()
valid_reports = ["daily", "weekly", "monthly"]

if report_type not in valid_reports:
    print("Invalid report type!")
    exit()

start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
end_date = input("Enter End Date (YYYY-MM-DD): ").strip()

# Previous Period Calculation
start = datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.strptime(end_date, "%Y-%m-%d")

days = (end - start).days + 1

previous_end = start - timedelta(days=1)
previous_start = previous_end - timedelta(days=days - 1)

previous_start = previous_start.strftime("%Y-%m-%d")
previous_end = previous_end.strftime("%Y-%m-%d")

# Database Connection
conn = sqlite3.connect("database/ecommerce.db")
cursor = conn.cursor()
print("\nGenerating Report...\n")


# Total Orders
query = """ SELECT COUNT(*) FROM orders WHERE DATE(order_date) BETWEEN ? AND ?;"""
cursor.execute(query, (start_date, end_date))
total_orders = cursor.fetchone()[0]


query = """ SELECT ROUND( SUM( oi.quantity * oi.unit_price *(1 - oi.discount_percent/100.0)),2)
FROM order_items oi JOIN orders o ON oi.order_id = o.order_id
WHERE DATE(o.order_date) BETWEEN ? AND ?;
"""

cursor.execute(query, (start_date, end_date))
total_revenue = cursor.fetchone()[0]
if total_revenue is None:
    total_revenue = 0

query = """SELECT COUNT(DISTINCT customer_id) FROM orders WHERE DATE(order_date) BETWEEN ? AND ?;"""
cursor.execute(query, (start_date, end_date))
unique_customers = cursor.fetchone()[0]

# -------------------------------
# Top 3 Products
# -------------------------------

query = """
SELECT p.product_name, SUM(oi.quantity) AS quantity FROM order_items oi 
JOIN products p
ON oi.product_id = p.product_id
JOIN orders o
ON oi.order_id = o.order_id
WHERE DATE(o.order_date) BETWEEN ? AND ?
GROUP BY p.product_name
ORDER BY quantity DESC
LIMIT 3;
"""

cursor.execute(query, (start_date, end_date))
top_products = cursor.fetchall()

query = """
SELECT ROUND( SUM( oi.quantity * oi.unit_price * (1 - oi.discount_percent/100.0)),2)
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
WHERE DATE(o.order_date) BETWEEN ? AND ?;
"""

cursor.execute(query, (previous_start, previous_end))
previous_revenue = cursor.fetchone()[0]
if previous_revenue is None:
    previous_revenue = 0


if previous_revenue > 0:
    change = ((total_revenue - previous_revenue)/ previous_revenue) * 100
else:
    change = 0


print("=" * 50)
print("Report Type :", report_type)
print("Date Range  :", start_date, "to", end_date)
print("=" * 50)
print(f"Total Orders      : {total_orders}")
print(f"Revenue           : {total_revenue:.2f}")
print(f"Unique Customers  : {unique_customers}")
print(f"Revenue Change %  : {change:.2f}")

print("\nTop 3 Products")

for product in top_products:
    print(f"{product[0]} - {product[1]}")

print("=" * 50)

conn.close()