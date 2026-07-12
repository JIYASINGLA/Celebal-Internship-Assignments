# E-Commerce Order Analytics System (Week 8 Celebal Assignment)

## Overview

The **E-Commerce Order Analytics System** is an end-to-end data analytics project developed using **Python, Pandas, SQLite, and SQL**. The project simulates a real-world e-commerce environment by generating realistic datasets with intentional inconsistencies, cleaning and validating the data, storing it in an SQLite database, and performing business analytics using SQL queries. A command-line reporting tool is also included to generate summary reports dynamically.


## Objective

Design and develop an end-to-end e-commerce analytics system that performs:

- Dataset Generation
- Data Cleaning & Validation
- Database Creation
- SQL Analytics
- Customer Segmentation
- Cohort & Retention Analysis
- CLI Report Generation
- Edge Case Testing


## Technologies Used

- Python 3
- Pandas
- Faker
- SQLite
- SQL
- VS Code


## Project Structure

```text
Week 8 Celebal Assignment (Ecommerce Mini Project)/
│── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── cleaned/
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       ├── orders_clean.csv
│       └── order_items_clean.csv
│
│── database/
│   └── ecommerce.db
│
│── output/
│   ├── issues_report.txt
│   └── sample_reports/
│
│── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_data.py
│   ├── report_cli.py
│   ├── run_queries.py
│   └── test_cases.py
│
│── sql/
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── intermediate.sql
│   ├── window_functions.sql
│   ├── cte_analysis.sql
│   └── cohort_analysis.sql
|
│── Week 8 Assignment Report.pdf
│── requirements.txt
│── README.md
```


## Project Workflow

```text
Generate Dataset
        ↓
Raw CSV Files
        ↓
Data Cleaning & Validation
        ↓
Cleaned CSV Files
        ↓
SQLite Database
        ↓
SQL Analytics
        ↓
CLI Reporting Tool
        ↓
Business Reports
```


## Features

- Generate realistic e-commerce datasets using Faker.
- Introduce intentional data inconsistencies for testing.
- Clean and validate data using Pandas.
- Validate email addresses and date formats.
- Check referential integrity between tables.
- Store cleaned data in SQLite.
- Perform SQL analytics using:
  - Joins
  - Aggregations
  - Window Functions
  - Common Table Expressions (CTEs)
- Customer Segmentation
- Cohort Analysis
- Retention Analysis
- Command-Line Reporting Tool
- Edge Case Testing


## SQL Reports

### Basic Analytics

- Total Revenue by Category
- Top 10 Customers
- Monthly Order Count

### Intermediate Analytics

- Customers Without Delivered Orders
- Products with More Returns than Purchases
- Return Rate by Category

### Advanced Analytics

- Running Revenue by Region
- Product Ranking using DENSE_RANK()
- Customer Order Gap using LAG()
- Monthly Customer Segmentation
- Customer Quartiles using NTILE()
- Revenue Contribution Analysis
- Year-over-Year Revenue Comparison
- First vs Latest Purchase Category
- Cohort Analysis
- Retention Rate Analysis


## How to Run

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Generate Dataset

```bash
python scripts/generate_data.py
```

### Clean Dataset

```bash
python scripts/clean_data.py
```

### Load Data into SQLite

```bash
python scripts/load_data.py
```

### Execute SQL Queries

```bash
python scripts/run_queries.py
```

### Generate Reports

```bash
python scripts/report_cli.py
```

### Run Test Cases

```bash
python scripts/test_cases.py
```


## Sample Outputs

The `output/sample_reports` folder contains screenshots of:

- Dataset Generation
- Raw CSV Files
- Data Cleaning
- Issues Report
- Cleaned CSV Files
- SQLite Database
- Revenue by Category
- Monthly Orders
- Top Customers
- Product Ranking
- Customer Quartiles
- Revenue Contribution
- Cohort Analysis
- Retention Rate
- Customer Segmentation
- CLI Report Execution
- CLI Top Customers Report
- CLI Retention Report


## Conclusion

The E-Commerce Order Analytics System demonstrates a complete data analytics workflow using Python and SQL. It covers dataset generation, data cleaning, database management, SQL analytics, customer segmentation, cohort analysis, and CLI-based reporting. This project provides practical experience in data processing, database operations, and business analytics.
