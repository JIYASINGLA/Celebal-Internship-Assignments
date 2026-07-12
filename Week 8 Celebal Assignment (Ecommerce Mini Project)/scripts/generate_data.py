import os
import random
import pandas as pd
from faker import Faker

fake = Faker()
random.seed(42)
Faker.seed(42)

RAW_DATA_PATH = os.path.join("data", "raw")
os.makedirs(RAW_DATA_PATH, exist_ok=True)

NUM_CUSTOMERS = 500
NUM_PRODUCTS = 500
NUM_ORDERS = 500
NUM_ORDER_ITEMS = 700

CUSTOMER_TYPES = ["REGULAR", "PREMIUM", "VIP"]

CUSTOMER_REGIONS = [
    "North",
    "South",
    "East",
    "West"
]

ORDER_REGIONS = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST"
]

ORDER_STATUS = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

CATEGORIES = {
    "Electronics": ["Laptop", "Mobile", "Headphones", "Monitor"],
    "Books": ["Novel", "Dictionary", "Magazine", "Notebook"],
    "Home": ["Chair", "Table", "Sofa", "Lamp"],
    "Clothing": ["Shirt", "Jeans", "Jacket", "T-Shirt"],
    "Sports": ["Football", "Bat", "Cricket Ball", "Tennis Racket"],
    "Beauty": ["Face Wash", "Perfume", "Lipstick", "Cream"]
}


# Utility Functions #

def save_csv(df, filename):
    """Save dataframe into raw folder."""
    path = os.path.join(RAW_DATA_PATH, filename)
    df.to_csv(path, index=False)
    print(f"{filename} saved ({len(df)} records)")

def inject_invalid_email(email):
    """Create malformed email for testing."""
    option = random.randint(1, 3)
    if option == 1:
        return email.replace("@", "")
    if option == 2:
        return email.split("@")[0] + "@"
    return "@" + email.split("@")[1]

def modify_product_name(name):
    """Create inconsistent product names."""
    option = random.randint(1, 3)
    if option == 1:
        return f"   {name}   "
    if option == 2:
        return name.upper()
    return name.swapcase()

# Customer Data #

def generate_customers():
    records = []
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        email = fake.email()
        if random.random() < 0.02:
            email = inject_invalid_email(email)
        records.append([
            customer_id,
            fake.name(),
            email,
            fake.date_between("-3y", "today"),
            random.choice(CUSTOMER_TYPES),
            random.choice(CUSTOMER_REGIONS)
        ])

    columns = [
        "customer_id",
        "customer_name",
        "email",
        "registration_date",
        "customer_type",
        "region"
    ]
    df = pd.DataFrame(records, columns=columns)
    save_csv(df, "customers.csv")
    return df


# Product Data #

def generate_products():
    records = []
    for product_id in range(1, NUM_PRODUCTS + 1):

        category = random.choice(list(CATEGORIES.keys()))
        subcategory = random.choice(CATEGORIES[category])
        product_name = subcategory

        if random.random() < 0.05:
            product_name = modify_product_name(product_name)

        records.append([
            product_id,
            product_name,
            category,
            subcategory,
            round(random.uniform(100, 5000), 2)
        ])

    columns = [
        "product_id",
        "product_name",
        "category",
        "subcategory",
        "cost_price"
    ]
    df = pd.DataFrame(records, columns=columns)
    save_csv(df, "products.csv")
    return df


# Orders #
def generate_orders():
    records = []
    for order_id in range(1, NUM_ORDERS + 1):
        customer_id = (
            None
            if random.random() < 0.05
            else random.randint(1, NUM_CUSTOMERS)
        )

        dt = fake.date_time_between("-2y", "now")

        if random.random() < 0.05:
            order_date = dt.strftime("%d-%m-%Y")
        else:
            order_date = dt.strftime("%Y-%m-%d %H:%M:%S")

        records.append([
            order_id,
            customer_id,
            order_date,
            random.choice(ORDER_STATUS),
            random.choice(ORDER_REGIONS)
        ])

    columns = [
        "order_id",
        "customer_id",
        "order_date",
        "status",
        "region_code"
    ]
    df = pd.DataFrame(records, columns=columns)
    save_csv(df, "orders.csv")
    return df


# Order Item #
def generate_order_items():
    records = []

    for item_id in range(1, NUM_ORDER_ITEMS + 1):

        # Generate Order ID (2% invalid)
        if random.random() < 0.02:
            order_id = NUM_ORDERS + random.randint(1, 20)
        else:
            order_id = random.randint(1, NUM_ORDERS)

        # Generate Product ID (1% invalid)
        if random.random() < 0.01:
            product_id = NUM_PRODUCTS + random.randint(1, 20)
        else:
            product_id = random.randint(1, NUM_PRODUCTS)

        # Quantity
        quantity = random.randint(1, 5)
        chance = random.random()

        if chance < 0.03:
            quantity = -random.randint(1, 3)
        elif chance < 0.05:
            quantity = 0

        # Unit Price
        unit_price = round(random.uniform(200, 8000), 2)

        # Discount
        discount = random.randint(0, 50)

        if random.random() < 0.02:
            discount = random.randint(101, 150)

        records.append([
            item_id,
            order_id,
            product_id,
            quantity,
            unit_price,
            discount
        ])

    columns = [
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount_percent"
    ]

    df = pd.DataFrame(records, columns=columns)

    save_csv(df, "order_items.csv")

    return df


def main():
    print("\nGenerating E-Commerce Dataset...\n")

    customers = generate_customers()
    products = generate_products()
    orders = generate_orders()
    order_items = generate_order_items()

    print("\nGeneration Completed Successfully\n")

    print("\nDataset Summary")
    print("-" * 30)
    print(f"Customers    : {len(customers)}")
    print(f"Products     : {len(products)}")
    print(f"Orders       : {len(orders)}")
    print(f"Order Items  : {len(order_items)}")


if __name__ == "__main__":
    main()