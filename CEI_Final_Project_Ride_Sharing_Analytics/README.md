# Ride-Sharing Analytics & Driver Performance Pipeline

## Celebal Technologies Excellence Internship 2026 – Final Project

## Project Overview

This project implements an end-to-end **Ride-Sharing Analytics & Driver Performance Pipeline** using **Apache Spark (PySpark)** on **Databricks** following the **Medallion Architecture (Bronze, Silver, and Gold layers)**.

The pipeline processes raw ride-sharing datasets, performs data cleaning and transformations, and generates business-ready analytics to evaluate driver performance, cancellations, delays, revenue, and ride demand. The implementation demonstrates a scalable data engineering workflow that converts raw operational data into actionable business insights.


## Objectives

- Track ride and driver activity.
- Analyze cancellations and delays.
- Identify high-demand pickup locations.
- Evaluate driver performance.
- Generate business-level KPIs.


## Technology Stack

- Python
- Apache Spark (PySpark)
- Databricks Community Edition
- Parquet File Format
- Medallion Architecture


## Dataset

The project uses the following datasets:

| Dataset | Description |
|----------|-------------|
| `drivers.csv` | Driver information including driver ID, name, city, and rating |
| `trips.csv` | Trip details including pickup, drop, distance, fare, and status |
| `trip_logs.csv` | Trip logs containing timestamps, delays, and cancellation information |



## Medallion Architecture

### Bronze Layer
- Reads raw CSV datasets.
- Stores data without any transformations.
- Saves datasets in Parquet format.

### Silver Layer
- Cleans and validates data.
- Removes duplicate records.
- Handles null values.
- Filters invalid records.
- Joins driver, trip, and trip log datasets.
- Creates derived columns:
  - Trip Duration
  - Completion Flag

### Gold Layer
Generates business-ready analytical datasets including:

- Driver Performance Metrics
- Cancellation Rate Analysis
- Delay Analysis
- Revenue Insights
- High-Demand Pickup Locations
- Driver Ranking


## Project Workflow

```text
              Raw CSV Files
      ┌──────────────┬──────────────┬
      │              │              │
 drivers.csv     trips.csv     trip_logs.csv
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │      Bronze Layer        │
        │   Store Raw Data         │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │      Silver Layer        │
        │ Cleaning & Validation    │
        │ Dataset Joins            │
        │ Derived Columns          │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │       Gold Layer         │
        │ Business KPIs            │
        │ Analytics Tables         │
        └──────────────────────────┘
                     │
                     ▼
          Business Insights & Reports
```


## Business KPIs

- Driver Performance Metrics
- Cancellation Rate per Driver
- Delay Analysis
- Revenue Analysis
- High-Demand Pickup Locations
- Driver Ranking using Window Functions


## Spark Optimizations

The project includes the following Spark optimization techniques:

- Parquet storage format for efficient data storage
- Repartitioning for optimized data distribution
- Query plan analysis using `explain(True)`
- Photon Execution support in Databricks


## Repository Structure

```text
Ride_Sharing_Analytics/
│
├── README.md
│
├── data/
│   ├── drivers.csv
│   ├── trips.csv
│   └── trip_logs.csv
│
├── notebooks/
│   └── Ride_Sharing_Analytics_Driver_Performance_Pipeline.ipynb
│
├── medallion_architecture/
│   ├── bronze/
│   │   ├── drivers/
│   │   ├── trips/
│   │   └── trip_logs/
│   │
│   ├── silver/
│   │   └── final_data/
│   │
│   └── gold/
│       ├── driver_performance/
│       ├── cancellation_rate/
│       ├── delay_analysis/
│       ├── high_demand_locations/
│       └── revenue_insights/
│
└── screenshots/
    ├── task1_read_datasets.png
    ├── task2_bronze_layer.png
    ├── task3_joined_data.png
    ├── task4_data_cleaning.png
    ├── task5_derived_columns.png
    ├── task6_filter_invalid_records.png
    ├── task7_silver_layer.png
    ├── task8_driver_performance.png
    ├── task9_cancellation_rate.png
    ├── task10_high_demand_locations.png
    ├── task11_revenue_insights.png
    ├── task11_delay_analysis.png
    ├── task12_gold_layer.png
    ├── task13_validation.png
    ├── task14_optimization.png
    ├── task15_driver_ranking.png
    └── final_validation.png
```


## Key Features

- End-to-end Data Engineering Pipeline
- Medallion Architecture Implementation
- PySpark-based Data Processing
- Data Cleaning & Validation
- Business KPI Generation
- Delay & Cancellation Analysis
- Revenue Analysis
- Driver Performance Evaluation
- Spark Window Functions
- Optimized Processing using Databricks


## Results

The pipeline successfully generates:

- Driver Performance Metrics
- Cancellation Rate per Driver
- Delay Analysis
- Revenue Insights
- High-Demand Pickup Locations
- Ranked Drivers based on Total Revenue


## Acknowledgement

This project was completed as the **Final Project** for the **Celebal Technologies Excellence Internship 2026**. It demonstrates the implementation of an end-to-end data engineering pipeline using **Apache Spark (PySpark)**, **Databricks**, and the **Medallion Architecture** to transform raw ride-sharing data into meaningful business insights.
