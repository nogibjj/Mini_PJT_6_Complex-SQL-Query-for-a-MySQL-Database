from databricks import sql
from dotenv import load_dotenv
import os

# Define a global variable for the log file
LOG_FILE = "query_log.md"

def log_query(query_text, query_result="none"):
    """Adds the SQL query and its result to a markdown log file"""
    with open(LOG_FILE, "a", encoding="utf-8") as file:  # Specify encoding
        file.write(f"```sql\n{query_text}\n```\n\n")
        file.write(f"```response from databricks\n{query_result}\n```\n\n")

# Query module for the HR database
complex_query = """
SELECT 
    p.EmployeeNumber, 
    p.Age, 
    p.Gender, 
    a.Attrition, 
    a.Department
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
ORDER BY 
    p.EmployeeNumber ASC;
"""

# Load environment variables for Databricks connection
load_dotenv()
server_hostname = os.getenv("SERVER_HOSTNAME")
access_token = os.getenv("DATABRICKS_KEY")
http_path = os.getenv("HTTP_PATH")

def run_query():
    """Execute a SQL query on Databricks SQL, print and log results."""
    # Connect to the Databricks SQL Warehouse
    with sql.connect(
        server_hostname=server_hostname, 
        http_path=http_path, 
        access_token=access_token
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(complex_query)
            query_result = cursor.fetchall()

            # Print each row from the result
            for row in query_result:
                print(row)

            # Log the query and its result
            log_query(complex_query, query_result)

            # Print success message
            print("Query completed successfully.")
            return "success"  

# Execute the complex query when the script runs
if __name__ == "__main__":
    result = run_query()
