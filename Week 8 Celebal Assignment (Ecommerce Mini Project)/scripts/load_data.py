import os
import sqlite3
import pandas as pd

# Configuration #

DATABASE_DIR = "database"
DATABASE_FILE = os.path.join(DATABASE_DIR, "ecommerce.db")
SCHEMA_FILE = os.path.join("sql", "schema.sql")
CLEANED_DATA_PATH = os.path.join("data", "cleaned")
TABLE_FILES = {
    "customers": "customers_clean.csv",
    "products": "products_clean.csv",
    "orders": "orders_clean.csv",
    "order_items": "order_items_clean.csv"
}
os.makedirs(DATABASE_DIR, exist_ok=True)


# Utility Functions #

def create_connection():
    """Create SQLite database connection."""
    return sqlite3.connect(DATABASE_FILE)

def create_tables(cursor):
    """Create database tables using schema.sql."""
    with open(SCHEMA_FILE, "r") as file:
        cursor.executescript(file.read())
    print("Tables Created Successfully")

def load_csv(filename):
    """Read a cleaned CSV file."""
    path = os.path.join(CLEANED_DATA_PATH, filename)
    return pd.read_csv(path)

def insert_table(df, table_name, connection):
    """Insert dataframe into SQLite table."""
    df.to_sql(
        table_name,
        connection,
        if_exists="append",
        index=False
    )
    print(f"{table_name} loaded successfully")

def display_table_counts(cursor):
    """Display number of records in each table."""
    print("\nDatabase Summary")
    print("-" * 30)
    for table in TABLE_FILES.keys():
        count = cursor.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        print(f"{table:<12}: {count}")


def main():
    print("\nConnecting to SQLite Database...\n")
    conn = create_connection()
    cursor = conn.cursor()
    create_tables(cursor)

    # Load datasets into SQLite
    for table_name, filename in TABLE_FILES.items():
        df = load_csv(filename)
        insert_table(
            df,
            table_name,
            conn
        )
    conn.commit()
    print("\nAll datasets loaded successfully.")
    display_table_counts(cursor)
    conn.close()
    print("\nDatabase connection closed.")
if __name__ == "__main__":
    main()