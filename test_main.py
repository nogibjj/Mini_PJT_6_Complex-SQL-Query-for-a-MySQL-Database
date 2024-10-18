"""
Test cases for data extraction, transformation, and querying
"""
from main import main_res


def test_extract():
    # Test to verify that data extraction was successful
    result = main_res()
    assert result["extract"] == "success", "Test for data extraction failed"


def test_transform():
    # Test to ensure data transformation and loading into the database
    result = main_res()
    assert result["transform_db"] == "success", "Test for database load failed"


def test_query():
    # Test to ensure that querying the database was successful
    result = main_res()
    assert result["query"] == "success", "Test for querying the database failed"


if __name__ == "__main__":
    # Run all tests
    test_extract()
    test_transform()
    test_query()
    print("All tests passed")
