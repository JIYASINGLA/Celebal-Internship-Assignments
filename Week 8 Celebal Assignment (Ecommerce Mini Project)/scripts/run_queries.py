import sqlite3

conn = sqlite3.connect("database/ecommerce.db")
cursor = conn.cursor()

sql_files = [
    "sql/aggregations.sql",
    "sql/intermediate.sql",
    "sql/window_functions.sql",
    "sql/cte_analysis.sql",
    "sql/cohort_analysis.sql"
]

for sql_file in sql_files:

    print("\n" + "=" * 80)
    print(f"Running {sql_file}")
    print("=" * 80)

    with open(sql_file, "r", encoding="utf-8") as file:
        queries = file.read().split(";")

    for query in queries:
        query = query.strip()

        if not query:
            continue

        print("-" * 70)

        try:
            rows = cursor.execute(query).fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("Query executed successfully.")

        except Exception as e:
            print("Error:", e)


conn.close()