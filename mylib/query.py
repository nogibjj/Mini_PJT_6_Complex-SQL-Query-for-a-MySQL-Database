# Step 3
# """Query the database"""

import sqlite3


def queryCreate():
    conn = sqlite3.connect("HR.db")
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS HR (
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

    # Insert data into the correct table and with correct placeholders
    cursor.execute(
        """
        INSERT INTO HR 
        (Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, 
        Education, EducationField, EmployeeCount, EmployeeNumber)
        VALUES(30, 'Yes', 'Travel_Rarely', 1100, 'Sales', 5, 3, 'Life Sciences', 1, 12345)
        """
    )

    # Commit the transaction
    conn.commit()
    conn.close()
    return "Create Success"


def queryRead():
    conn = sqlite3.connect("HR.db")
    cursor = conn.cursor()

    # Read and fetch results from the HR table, limit the results
    cursor.execute("SELECT * FROM HR")
    # results = cursor.fetchall()  # Fetch the result of the query

    conn.close()
    return "Read Success"


def queryUpdate():
    conn = sqlite3.connect("HR.db")
    cursor = conn.cursor()

    # Update the data and commit the changes
    cursor.execute(
         """
        UPDATE HR
        SET 
            Age = CASE
                    WHEN Age IS NULL OR Age = '' THEN 9999999
                    ELSE Age
                END,
            Attrition = CASE
                    WHEN Attrition IS NULL OR Attrition = '' THEN '9999999'
                    ELSE Attrition
                END,
            BusinessTravel = CASE
                    WHEN BusinessTravel IS NULL OR BusinessTravel = '' THEN '9999999'
                    ELSE BusinessTravel
                END,
            DailyRate = CASE
                    WHEN DailyRate IS NULL OR DailyRate = '' THEN 9999999
                    ELSE DailyRate
                END,
            Department = CASE
                    WHEN Department IS NULL OR Department = '' THEN '9999999'
                    ELSE Department
                END,
            DistanceFromHome = CASE
                    WHEN DistanceFromHome IS NULL OR DistanceFromHome = '' THEN 9999999
                    ELSE DistanceFromHome
                END,
            Education = CASE
                    WHEN Education IS NULL OR Education = '' THEN 9999999
                    ELSE Education
                END,
            EducationField = CASE
                    WHEN EducationField IS NULL OR EducationField = '' THEN '9999999'
                    ELSE EducationField
                END,
            EmployeeCount = CASE
                    WHEN EmployeeCount IS NULL OR EmployeeCount = '' THEN 9999999
                    ELSE EmployeeCount
                END,
            EmployeeNumber = CASE
                    WHEN EmployeeNumber IS NULL OR EmployeeNumber = '' THEN 9999999
                    ELSE EmployeeNumber
                END
        WHERE id = 1
        """
    )


    conn.commit()  # Commit the update
    conn.close()
    return "Update Success"


def queryDelete():
    conn = sqlite3.connect("HR.db")
    cursor = conn.cursor()

    # Delete the record and commit the changes
    cursor.execute("DELETE FROM HR WHERE id = 3")

    conn.commit()  # Commit the deletion
    conn.close()
    return "Delete Success"


if __name__ == "__main__":
    print(queryCreate())
    print(queryRead())
    print(queryUpdate())
    print(queryDelete())
