import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv


def load_data_to_db(dataset_personal="HR_1.csv", dataset_attrition="HR_2.csv"):
    """
    Load data from CSV files and insert it into Databricks SQL Warehouse tables.
    This script processes two datasets: 'hr_personal_data' and 'hr_attrition_data'.
    """

    # Step 1: Load CSV data using pandas
    df_personal_data = pd.read_csv(dataset_personal)
    df_attrition_data = pd.read_csv(dataset_attrition)

    # Step 2: Load environment variables for database connection
    load_dotenv()
    server_hostname = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http")

    # Step 3: Connect to Databricks SQL Warehouse
    with sql.connect(
        server_hostname=server_hostname, http_path=http_path, access_token=access_token
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
            for _, row in df_personal_data.iterrows():
                # Skip rows with missing (None) values
                if row.isnull().any():
                    print(f"Skipping row due to missing values: {row}")
                    continue
                values = (
                    row["EmployeeNumber"],
                    row["Age"],
                    row["Gender"],
                    row["Education"],
                )
                c.execute(
                    """
                    INSERT INTO hr_personal_data (EmployeeNumber, Age, Gender, Education)
                    VALUES (?, ?, ?, ?)
                """,
                    values,
                )
            print("Finished inserting data into hr_personal_data.")

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
            for _, row in df_attrition_data.iterrows():
                # Skip rows with missing (None) values
                if row.isnull().any():
                    print(f"Skipping row due to missing values: {row}")
                    continue
                values = (
                    row["EmployeeNumber"],
                    row["Department"],
                    row["JobRole"],
                    row["Attrition"],
                )
                c.execute(
                    """
                    INSERT INTO hr_attrition_data (EmployeeNumber, Department, JobRole, Attrition)
                    VALUES (?, ?, ?, ?)
                """,
                    values,
                )

            # Step 9: Commit the changes to the database
            conn.commit()
            conn.close()
            print("Finished inserting data into hr_attrition_data.")
            return "Data inserted successfully."

if __name__ == "__main__":
    load_data_to_db()
