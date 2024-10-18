# IDS-706 Data Engineering Assignment
## Mini Project 6 : Complex SQL Query for a MySQL Database (Databricks)

#### Status(CI/CD) badge  [![CI](https://github.com/nogibjj/Mini_PJT_6_Complex-SQL-Query-for-a-MySQL-Database/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/Mini_PJT_6_Complex-SQL-Query-for-a-MySQL-Database/actions/workflows/CICD.yml)
------

### Project Purpose 

- The goal of this project is to build an Extract, Transform, Load (ETL), and Query pipeline using Python and Databricks.

- The project involves importing human resource-related data from an external source, extracting specific columns, separating the data into two files, establishing a connection to Databricks, and running SQL queries to perform joins, aggregations, and sorting operations.

-----

### Requirements

* ***Design a complex SQL query involving joins, aggregation, and sorting***
* ***Provide an explanation for what the query is doing and the expected results***

### Deliverables

* ***SQL query***
* ***Written explanation of the query***

---------
### Dataset
File name : [HR_1.csv](HR_1.csv), [HR_2.csv](HR_2.csv) save in data_raw folder
 - The data used in this project originlly come from IBM.  

----------
### Extract & Transform & Query
* Extract : The process retrieves two datasets(`HR_1.csv`, `HR_2.csv`) from an external source.

    - The `extract` function downloads two CSV files from specified URLs and saves them locally as HR_1.csv and HR_2.csv. To save computatinoal efficiency, only 8 out of the 35 total columns are selected and saved. If the process succeeds.

* Transform : This step extracts the necessary columns and uploads the data to the Databricks SQL Warehouse.

    - The `df_personal_data` DataFrame contains the columns "EmployeeNumber," "Age," "Gender," and "Education.", while the `df_attrition_data` DataFrame includes "EmployeeNumber," "Department," "JobRole," and "Attrition." Both DataFrames consist of 4 columns with 1,471 rows each.

    - Using the `sql.connect()` method, the script connects to Databricks SQL Warehouse with a unique token and creates the two tables(`hr_attrition_data`,`hr_personal_data`). EmployeeNumber is defined as the unique index in both tables.


* Query : The SQL query performs `joins`, `aggregation`, and `sorting` operations on the data stored in Databricks, and logs the results.

    - The `log_query` function records the executed SQL query and its result in the `query_log.md` file.

    - The SQL query joins the `hr_personal_data` and `hr_attrition_data` tables using EmployeeNumber to calculate the total number of employees (TotalEmployees) and attrition count (TotalAttrition) for each department.

    - The query uses a **LEFT JOIN** to merge the two tables on the `EmployeeNumber` field. It calculates the total number of employees in each department using `COUNT(p.EmployeeNumber)`, and the total number of attrition cases by counting the `Attrition` field where the value is "Yes." The results are grouped by department using **GROUP BY**, and sorted alphabetically by department name using **ORDER BY**.
        
        [Query log]
        ![Query](Screenshot.png)

        [Query output]
        ![Query_output](query_output.png)

### File structure
```
Mini_PJT_6_Complex-SQL-Query-for-a-MySQL-Database
├─ .devcontainer
│  ├─ Dockerfile
│  └─ devcontainer.json
├─ .github
│  └─ workflows
│     └─ CICD.yml
├─ HR_1.csv
├─ HR_2.csv
├─ Makefile
├─ README.md
├─ data_raw
│  ├─ HR_1.csv
│  └─ HR_2.csv
├─ main.py
│  ├─ extract.py
│  ├─ query.py
│  └─ transform.py
├─ query_log.md
├─ query_log_image.png
├─ requirements.txt
└─ test_main.py

```