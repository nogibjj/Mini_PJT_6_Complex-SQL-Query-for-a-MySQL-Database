import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load_data_to_db(dataset_personal="HR_1.csv", dataset_attrition="HR_2.csv"):
    """
    Load data from CSV files and insert it into Databricks SQL Warehouse tables.
    This script processes two datasets: 'hr_personal_data' and 'hr_attrition_data'.
    """
    # Step 1: Load CSV data using pandas, only selecting relevant columns
    df_personal_data = pd.read_csv(dataset_personal)[
        ['EmployeeNumber', 'Age', 'Gender', 'Education']
    ]
    df_attrition_data = pd.read_csv(dataset_attrition)[
        ['EmployeeNumber', 'Department', 'JobRole', 'Attrition']
    ]

    # Step 2: Load environment variables for database connection
    load_dotenv()
    server_hostname = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http")

    # Step 3: Connect to Databricks SQL Warehouse
    with sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    ) as conn:

        with conn.cursor() as c:
            # Step 4: Drop existing tables if they already exist
            c.execute("DROP TABLE IF EXISTS hr_personal_data")
            c.execute("DROP TABLE IF EXISTS hr_attrition_data")

            # Step 5: Create 'hr_personal_data' table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS hr_personal_data (
                    EmployeeNumber INT,
                    Age INT,
                    Gender STRING,
                    Education STRING
                )
                """
            )

            # Step 6: Insert data into 'hr_personal_data' table
            if not df_personal_data.empty:
                values = [tuple(row) for row in df_personal_data.values]
                string_sql = (
                    "INSERT INTO hr_personal_data "
                    "(EmployeeNumber, Age, Gender, Education) VALUES"
                )
                string_sql += "\n" + ",\n".join([str(v) for v in values]) + ";"
                c.execute(string_sql)
                print("Finished batch inserting data into hr_personal_data.")

            # Step 7: Create 'hr_attrition_data' table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS hr_attrition_data (
                    EmployeeNumber INT,
                    Department STRING,
                    JobRole STRING,
                    Attrition STRING
                )
                """
            )

            # Step 8: Insert data into 'hr_attrition_data' table 
            if not df_attrition_data.empty:
                values = [tuple(row) for row in df_attrition_data.values]
                string_sql = (
                    "INSERT INTO hr_attrition_data "
                    "(EmployeeNumber, Department, JobRole, Attrition) VALUES"
                )
                string_sql += "\n" + ",\n".join([str(v) for v in values]) + ";"
                c.execute(string_sql)
                print("Finished batch inserting data into hr_attrition_data.")

            # Step 9: Commit the changes to the database
            conn.commit()
            print("Data successfully inserted into both tables.")
            return "success"

if __name__ == "__main__":
    result = load_data_to_db()
