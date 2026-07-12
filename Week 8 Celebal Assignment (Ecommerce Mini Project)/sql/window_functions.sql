-- Query 7: Running Total of Revenue per Region
WITH daily_revenue AS
(
    SELECT o.region_code,
        DATE(o.order_date) AS order_date,
        ROUND(
            SUM(oi.quantity * oi.unit_price *(1 - oi.discount_percent / 100.0)),
            2
        ) AS daily_revenue
    FROM orders o
    JOIN order_items oi
    ON o.order_id = oi.order_id
    GROUP BY o.region_code, DATE(o.order_date)
)

SELECT region_code, order_date, daily_revenue,
    SUM(daily_revenue) OVER
    (
        PARTITION BY region_code
        ORDER BY order_date
    ) AS running_total
FROM daily_revenue
ORDER BY region_code, order_date;

-- Query 8: Product Ranking
WITH revenue AS
(
    SELECT p.category, p.product_name,
        ROUND(
            SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent /100.0)),
            2
        ) AS total_revenue
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    GROUP BY p.category, p.product_name
)

SELECT category, product_name, total_revenue,
    DENSE_RANK() OVER
    (
        PARTITION BY category
        ORDER BY total_revenue DESC
    ) AS rank_in_category
FROM revenue
ORDER BY category, rank_in_category;

-- Query 9: Days Between Consecutive Orders
WITH customer_orders AS
(
    SELECT customer_id, order_date, LAG(order_date) OVER
        (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
    WHERE customer_id <> 'Unknown'
)

SELECT customer_id, order_date, previous_order_date,
    ROUND(
        julianday(order_date) -
        julianday(previous_order_date),
        2
    ) AS days_gap
FROM customer_orders;

-- Query 9 (Part 2): At Risk Customers
WITH customer_orders AS
(
    SELECT customer_id, order_date, LAG(order_date) OVER
        (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
    WHERE customer_id <> 'Unknown'
),
gaps AS
(
    SELECT customer_id,
        julianday(order_date) -
        julianday(previous_order_date)
        AS days_gap
    FROM customer_orders
    WHERE previous_order_date IS NOT NULL
)

SELECT customer_id,
    ROUND(AVG(days_gap),2)
    AS average_gap,
    CASE
        WHEN AVG(days_gap) > 30
        THEN 'At Risk'
        ELSE 'Active'
    END AS customer_status
FROM gaps
GROUP BY customer_id
ORDER BY average_gap DESC;