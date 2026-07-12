DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;

CREATE TABLE customers(
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    email TEXT,
    registration_date TEXT,
    customer_type TEXT,
    region TEXT
);

CREATE TABLE products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    subcategory TEXT,
    cost_price REAL
);

CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,
    customer_id TEXT,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    region_code TEXT NOT NULL,
    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER,
    unit_price REAL,
    discount_percent REAL,
    FOREIGN KEY(order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);