from mylib.extract import extract
from mylib.transform import load_data_to_db
from mylib.query import run_query

# Test to verify that data extraction was successful
def test_extract():
    # Call the extract function and store the result
    result = extract()

    # Assert that the extraction result is successful
    assert result == "success", "Test for data extraction failed"
    print("Extract test passed")


# Test to ensure data transformation and loading into the database
def test_transform():
    # Call the load_data_to_db function and store the result
    result = load_data_to_db()

    # Assert that the transformation and load result is successful
    assert result == "success", "Test for data transformation and load failed"
    print("Transform test passed")


# Test to ensure that querying the database was successful
def test_query():
    # Call the run_query function and store the result
    result = run_query()

    # Assert that the query result is successful
    assert result == "success", "Test for querying the database failed"
    print("Query test passed")


if __name__ == "__main__":
    # Run all tests
    test_extract()
    test_transform()
    test_query()
    print("All tests passed successfully")


# import json


# def test_extract():
#     # Load saved results from the JSON file
#     with open("results.json", "r") as file:
#         result = json.load(file)

#     # Test to verify that data extraction was successful
#     assert result["extract"] == "success", "Test for data extraction failed"


# def test_transform():
#     # Load saved results from the JSON file
#     with open("results.json", "r") as file:
#         result = json.load(file)

#     # Test to ensure data transformation and loading into the database
#     assert (
#         result["transform_db"] == "success"
#     ), "Test for data transformation and load failed"


# def test_query():
#     # Load saved results from the JSON file
#     with open("results.json", "r") as file:
#         result = json.load(file)

#     # Test to ensure that querying the database was successful
#     assert result["query"] == "success", "Test for querying the database failed"


# if __name__ == "__main__":
#     # Run all tests
#     test_extract()
#     test_transform()
#     test_query()
#     print("All tests passed")


#### Test time takes forever...Thus, I utilize json extention file to save calculation
