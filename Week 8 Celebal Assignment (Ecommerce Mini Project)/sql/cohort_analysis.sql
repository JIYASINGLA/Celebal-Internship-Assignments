-- Query 15: Cohort Analysis
WITH customer_cohort AS
(
    SELECT c.customer_id, DATE(c.registration_date) AS registration_date, DATE(o.order_date) AS order_date, strftime('%Y-%m', c.registration_date) AS cohort_month,
        (
            (CAST(strftime('%Y', o.order_date) AS INTEGER) -
             CAST(strftime('%Y', c.registration_date) AS INTEGER)) * 12
            +
            (CAST(strftime('%m', o.order_date) AS INTEGER) -
             CAST(strftime('%m', c.registration_date) AS INTEGER))
        ) AS month_number
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    WHERE o.customer_id <> 'Unknown'
)
SELECT cohort_month,
    COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) AS month_0,
    COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_id END) AS month_1,
    COUNT(DISTINCT CASE WHEN month_number = 2 THEN customer_id END) AS month_2,
    COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_id END) AS month_3
FROM customer_cohort
GROUP BY cohort_month
ORDER BY cohort_month;

-- Query 16: Retention Rate
WITH customer_cohort AS
(
    SELECT c.customer_id, strftime('%Y-%m', c.registration_date) AS cohort_month,
        (
            (CAST(strftime('%Y', o.order_date) AS INTEGER) -
             CAST(strftime('%Y', c.registration_date) AS INTEGER)) * 12
            +
            (CAST(strftime('%m', o.order_date) AS INTEGER) -
             CAST(strftime('%m', c.registration_date) AS INTEGER))
        ) AS month_number
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
),
cohort_size AS
(
    SELECT cohort_month, COUNT(DISTINCT customer_id) AS total_customers
    FROM customer_cohort
    WHERE month_number = 0
    GROUP BY cohort_month
)
SELECT cc.cohort_month, cc.month_number, COUNT(DISTINCT cc.customer_id) AS retained_customers, cs.total_customers,
    ROUND(COUNT(DISTINCT cc.customer_id) * 100.0 / cs.total_customers, 2)
AS retention_rate
FROM customer_cohort cc
JOIN cohort_size cs
ON cc.cohort_month = cs.cohort_month
GROUP BY cc.cohort_month, cc.month_number, cs.total_customers
ORDER BY cc.cohort_month, cc.month_number;