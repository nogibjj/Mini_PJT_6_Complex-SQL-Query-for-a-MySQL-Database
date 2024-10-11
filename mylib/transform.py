import sqlite3
import csv

def load(dataset="HR.csv"):
    # Open and read the dataset
    with open(dataset, newline="", encoding="utf-8", errors="ignore") as file:
        payload = csv.reader(file, delimiter=",")

        # Create a connection to SQLite3 database
        conn = sqlite3.connect("HR.db")
        c = conn.cursor()

        # Drop the existing table if it exists and create a new HR table
        c.execute("DROP TABLE IF EXISTS hr_data")
        c.execute(
            """
            CREATE TABLE hr_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Age INTEGER,
                Attrition TEXT,
                BusinessTravel TEXT,
                DailyRate INTEGER,
                Department TEXT,
                DistanceFromHome INTEGER,
                Education INTEGER,
                EducationField TEXT,
                EmployeeCount INTEGER,
                EmployeeNumber INTEGER
            )
            """
        )

        # Skip the header and insert the first 10 columns of data into the table
        next(payload)  # Skip the header row
        
        for row in payload:
            # Ensure row has at least 10 columns
            if len(row) >= 10:
                trimmed_row = row[:10]
                try:
                    # Insert the row into the database
                    c.execute(
                        """
                        INSERT INTO hr_data 
                        (Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, 
                        Education, EducationField, EmployeeCount, EmployeeNumber)
                        VALUES(?,?,?,?,?,?,?,?,?,?)
                        """,
                        trimmed_row
                    )
                except sqlite3.Error as e:
                    print(f"Error inserting row: {row} with error {e}")

        # Commit and close the connection
        conn.commit()
        conn.close()

    return "HR.db"

if __name__ == "__main__":
    load()
