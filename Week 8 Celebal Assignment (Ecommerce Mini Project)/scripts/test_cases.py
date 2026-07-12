import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("database/ecommerce.db")
cursor = conn.cursor()
print("=" * 60)
print("Running Edge Case Tests")
print("=" * 60)

# Test 1: Invalid Order ID References
print("\nTest 1: Invalid Order References")
query = """SELECT * FROM order_items WHERE order_id NOT IN ( SELECT order_id FROM orders); """
rows = cursor.execute(query).fetchall()
if rows:
    print("FAILED")
    print(f"Found {len(rows)} invalid order references.")
else:
    print("PASSED")
    print("No invalid order references found.")

# Test 2: Discount Greater Than 100%
print("\nTest 2: Discount > 100")
query = """ SELECT * FROM order_items WHERE discount_percent > 100; """
rows = cursor.execute(query).fetchall()
if rows:
    print("FAILED")
    print(f"Found {len(rows)} records with discount > 100.")
else:
    print("PASSED")
    print("No invalid discounts found.")

# Test 3: Quantity = 0
print("\nTest 3: Quantity = 0")
query = """ SELECT * FROM order_items WHERE quantity = 0; """
rows = cursor.execute(query).fetchall()
if rows:
    print("FAILED")
    print(f"Found {len(rows)} records with zero quantity.")
else:
    print("PASSED")
    print("No zero quantity records found.")

# Test 4: Future Order Dates
print("\nTest 4: Future Order Dates")
query = """ SELECT * FROM orders WHERE DATE(order_date) > DATE('now'); """
rows = cursor.execute(query).fetchall()
if rows:
    print("FAILED")
    print(f"Found {len(rows)} future order dates.")
else:
    print("PASSED")
    print("No future order dates found.")

print("\n" + "=" * 60)
print("All Test Cases Completed")
print("=" * 60)

conn.close()