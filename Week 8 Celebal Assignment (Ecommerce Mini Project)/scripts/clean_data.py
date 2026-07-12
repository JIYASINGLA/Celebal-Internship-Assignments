import os
import re
import pandas as pd

# Configuration #
RAW_DATA_PATH = os.path.join("data", "raw")
CLEANED_DATA_PATH = os.path.join("data", "cleaned")
OUTPUT_PATH = "output"
os.makedirs(CLEANED_DATA_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)
issues = []


# Utility Functions #
def load_data(filename):
    path = os.path.join(RAW_DATA_PATH, filename)
    return pd.read_csv(path)

def save_data(df, filename):
    path = os.path.join(CLEANED_DATA_PATH, filename)
    df.to_csv(path, index=False)
    print(f"{filename} created")

def save_issue(message):
    issues.append(message)

# Orders
def clean_orders(df):
    df = df.copy()
    df["customer_id"] = (
        df["customer_id"]
        .fillna("Unknown")
        .apply(
            lambda x: str(int(float(x)))
            if x != "Unknown"
            else "Unknown"
        )
    )
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )
    invalid_dates = df["order_date"].isna().sum()
    save_issue(f"Invalid order dates: {invalid_dates}")
    df["order_date"] = df["order_date"].dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    return df

# Products
def clean_products(df):
    df = df.copy()
    df["product_name"] = (
        df["product_name"]
        .str.strip()
        .str.title()
    )
    duplicate_products = df["product_name"].duplicated().sum()
    save_issue(
        f"Duplicate product names after cleaning: {duplicate_products}"
    )
    return df

# Customers
def clean_customers(df):
    df = df.copy()

    df["customer_id"] = (
        df["customer_id"]
        .astype(int)
        .astype(str)
    )

    df["customer_name"] = (
        df["customer_name"]
        .str.strip()
        .str.title()
    )

    return df

def validate_emails(df):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    invalid_customers = []
    for _, row in df.iterrows():
        email = str(row["email"])
        if not re.match(pattern, email):
            invalid_customers.append(row["customer_id"])
    save_issue(
        f"Invalid emails found: {len(invalid_customers)}"
    )
    return invalid_customers

# Order Items
def clean_order_items(df):
    df = df.copy()
    negative_qty = (df["quantity"] < 0).sum()
    zero_qty = (df["quantity"] == 0).sum()
    save_issue(
        f"Negative quantity records: {negative_qty}"
    )
    save_issue(
        f"Zero quantity records: {zero_qty}"
    )
    return df


def validate_discount(df):
    invalid = df[df["discount_percent"] > 100]
    save_issue(
        f"Discount greater than 100: {len(invalid)}"
    )
    return invalid

# Duplicate Removal
def remove_duplicates(df, table_name):
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    save_issue(
        f"{table_name}: Duplicate rows removed = {removed}"
    )
    return df

# Referential Integrity
def check_referential_integrity(
    order_items_df,
    orders_df
):

    valid_order_ids = set(
        orders_df["order_id"]
    )

    invalid_orders = order_items_df[
        ~order_items_df["order_id"].isin(
            valid_order_ids
        )
    ]

    save_issue(
        f"Invalid order references: {len(invalid_orders)}"
    )

    return invalid_orders

# Save Report
def save_report():
    report_path = os.path.join(
        OUTPUT_PATH,
        "issues_report.txt"
    )
    with open(report_path, "w") as file:
        for issue in issues:
            file.write(issue + "\n")
    print("issues_report.txt created")

def main():
    print("\nLoading datasets...\n")
    customers = load_data("customers.csv")
    products = load_data("products.csv")
    orders = load_data("orders.csv")
    order_items = load_data("order_items.csv")

    # Clean datasets
    customers = clean_customers(customers)
    products = clean_products(products)
    orders = clean_orders(orders)
    order_items = clean_order_items(order_items)

    # Remove duplicates
    customers = remove_duplicates(customers,"Customers")
    products = remove_duplicates(products, "Products")
    orders = remove_duplicates(orders, "Orders")
    order_items = remove_duplicates(order_items, "Order Items")

    # Validation
    invalid_email_customers = validate_emails(customers)
    validate_discount(order_items)

    invalid_orders = check_referential_integrity(order_items, orders)

    # Save cleaned files
    save_data(customers, "customers_clean.csv")
    save_data(products, "products_clean.csv")
    save_data(orders, "orders_clean.csv")
    save_data(order_items, "order_items_clean.csv")


    # Save report
    save_report()

    # Display Results
    print("\nInvalid Email Customer IDs")
    print(invalid_email_customers)
    print("\nInvalid Order References")
    print(invalid_orders)
    print("\nCleaning Summary")
    print("-" * 35)
    print(f"Customers      : {len(customers)}")
    print(f"Products       : {len(products)}")
    print(f"Orders         : {len(orders)}")
    print(f"Order Items    : {len(order_items)}")
    print(f"Invalid Emails : {len(invalid_email_customers)}")
    print(f"Invalid Orders : {len(invalid_orders)}")

    print("\nData Cleaning Completed Successfully!")


if __name__ == "__main__":
    main()