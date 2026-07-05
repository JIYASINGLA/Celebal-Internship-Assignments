# Delta Lake MERGE Implementation

## Overview

This project demonstrates incremental data processing using **Delta Lake** in **Databricks Community Edition**. The implementation uses the **Superstore Dataset** to perform data cleaning, create a Delta table, simulate incremental data, apply the **MERGE** operation, and validate the final output.


## Objective

The objective of this assignment is to perform incremental data processing using Delta Lake by:

- Loading a dataset into a Delta table.
- Performing basic data cleaning.
- Creating an incremental dataset.
- Applying the MERGE operation to update and insert records.
- Validating the final dataset.
- Displaying the final results.


## Dataset

- **Dataset Name:** Superstore Dataset
- **Source:** Kaggle
- **Format:** CSV

The dataset contains retail sales information, including customer details, product information, sales, quantity, discount, and profit.


## Tools & Technologies Used

- Databricks Community Edition
- Apache Spark (PySpark)
- Delta Lake
- Python
- GitHub


## Project Structure

```text
delta-lake-assignment/
│
├── data/
│   ├── Superstore.csv
│   └── superstore_incremental.csv
│
├── notebooks/
│   └── delta_merge_assignment.ipynb
│
├── screenshots/
│   ├── data_loading/
│   ├── data_cleaning/
│   ├── scd1/
│   ├── scd2/
│   ├── validation/
│   └── final_output/
│
├── report/
│   └── assignment_summary.pdf
│
└── README.md
```


## Implementation Steps

### Step 1: Load Dataset
- Read the Superstore CSV file using PySpark.
- Display the dataset.
- Verify schema and record count.

### Step 2: Data Cleaning
- Check for null values.
- Handle missing values (if any).
- Remove duplicate records.

### Step 3: Create Delta Table
- Convert the cleaned DataFrame into a Delta table.
- Save and read the Delta table.

### Step 4: Create Incremental Dataset
- Create a second dataset containing:
  - One updated record.
  - One new record.

### Step 5: Apply MERGE Operation
- Update existing records.
- Insert new records into the Delta table.

### Step 6: Validate Results
- Display the updated Delta table.
- Verify the final row count.
- Check for duplicate Order IDs.


## Results

- Successfully loaded the Superstore dataset into a Delta table.
- Performed data cleaning by checking null values and removing duplicates.
- Created an incremental dataset.
- Applied the Delta Lake MERGE operation.
- Updated existing records and inserted new records successfully.
- Validated the final dataset by checking row count and duplicate Order IDs.


## Learning Outcomes

Through this assignment, I learned:

- Working with Spark DataFrames.
- Data cleaning using PySpark.
- Creating Delta tables.
- Performing incremental data processing.
- Using Delta Lake MERGE.
- Validating data after updates.
- Understanding real-world ETL workflows.
