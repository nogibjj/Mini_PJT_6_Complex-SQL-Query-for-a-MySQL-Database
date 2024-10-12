"""
Test cases for data extraction, transformation, and CRUD operations
"""
from main import main_res


def test_extract():
    # Update the test to reflect the two CSV files
    result = main_res()
    assert result["extract_personal"] == "HR_1.csv", "Test for extracting HR_1.csv failed"
    assert result["extract_attrition"] == "HR_2.csv", "Test for extracting HR_2.csv failed"


def test_transform():
    # Ensure the transformation step applies to both datasets
    result = main_res()
    assert result["transform_db"] == "HR.db", "Test for database load failed"


def test_create():
    # Ensure the create operation succeeded for both datasets
    result = main_res()
    assert result["create"] == "Create Success", "Test for queryCreate() failed"


def test_read():
    # Ensure reading operation works for both tables in the database
    result = main_res()
    assert result["read"] == "Read Success", "Test for queryRead() failed"


def test_update():
    # Ensure the update operation works for both tables
    result = main_res()
    assert result["update"] == "Update Success", "Test for queryUpdate() failed"


def test_delete():
    # Ensure the delete operation works for both tables
    result = main_res()
    assert result["delete"] == "Delete Success", "Test for queryDelete() failed"


if __name__ == "__main__":
    test_extract()
    test_transform()
    test_create()
    test_read()
    test_update()
    test_delete()
    print("All tests passed!")
