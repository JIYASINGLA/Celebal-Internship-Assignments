-- Query 10: Monthly Customer Segmentation
WITH monthly_revenue AS
(
    SELECT o.customer_id, strftime('%Y-%m', o.order_date) AS order_month,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    WHERE o.customer_id <> 'Unknown'
    GROUP BY o.customer_id, order_month
),
customer_segment AS
(
    SELECT customer_id, order_month, revenue,
        CASE
            WHEN revenue > 10000 THEN 'High'
            WHEN revenue BETWEEN 5000 AND 10000 THEN 'Medium'
            ELSE 'Low'
        END AS segment
    FROM monthly_revenue
)
SELECT order_month, segment,
    COUNT(customer_id) AS total_customers
FROM customer_segment
GROUP BY order_month, segment
ORDER BY order_month, segment;

-- Query 11: Customer Quartiles
WITH customer_value AS
(
    SELECT o.customer_id,
        ROUND(
            SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)),2) AS total_value
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    WHERE o.customer_id <> 'Unknown'
    GROUP BY o.customer_id
)

SELECT customer_id, total_value,
    NTILE(4) OVER(ORDER BY total_value DESC
    ) AS quartile,
    CASE
        WHEN NTILE(4) OVER (ORDER BY total_value DESC)=1
            THEN 'Platinum'
        WHEN NTILE(4) OVER (ORDER BY total_value DESC)=2
            THEN 'Gold'
        WHEN NTILE(4) OVER (ORDER BY total_value DESC)=3
            THEN 'Silver'
        ELSE 'Bronze'
    END AS quartile_label
FROM customer_value;

-- Query 12: YoY Revenue Comparison
WITH yearly_revenue AS
(
    SELECT strftime('%Y', order_date) AS year, strftime('%m', order_date) AS month,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent /100.0)) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY year, month
)
SELECT current.year, current.month,
    ROUND(current.revenue,2) AS revenue,
    ROUND(previous.revenue,2) AS prev_year_revenue,
    ROUND(((current.revenue - previous.revenue) / previous.revenue) *100,2) AS yoy_growth_percent
FROM yearly_revenue current
LEFT JOIN yearly_revenue previous
ON current.month = previous.month
AND current.year = CAST(previous.year AS INTEGER)+1;

-- Query 13: First and Latest Category
WITH customer_category AS
(
    SELECT o.customer_id, p.category, o.order_date,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.order_date) AS first_order,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY o.order_date DESC) AS last_order
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
)

SELECT first.customer_id, first.category AS first_category, last.category AS latest_category,
    CASE
        WHEN first.category = last.category
            THEN 'No'
        ELSE 'Yes'
    END AS category_shift
FROM customer_category first
JOIN customer_category last
ON first.customer_id = last.customer_id
WHERE first.first_order=1
AND last.last_order=1;

-- Query 14: Revenue Contribution
WITH revenue AS
(
    SELECT o.customer_id,
        SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent/100.0)) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id=oi.order_id
    GROUP BY o.customer_id
)

SELECT customer_id,
    ROUND(revenue,2) AS revenue,
    ROUND(
        SUM(revenue) OVER (ORDER BY revenue DESC),2) AS cumulative_revenue,
    ROUND(CUME_DIST() OVER (ORDER BY revenue DESC)*100,2) AS cumulative_percent
FROM revenue
ORDER BY revenue DESC;