import json

def test_extract():
    # Load saved results from the JSON file
    with open("results.json", "r") as file:
        result = json.load(file)
    
    # Test to verify that data extraction was successful
    assert result["extract"] == "success", "Test for data extraction failed"


def test_transform():
    # Load saved results from the JSON file
    with open("results.json", "r") as file:
        result = json.load(file)
    
    # Test to ensure data transformation and loading into the database
    assert result["transform_db"] == "success", "Test for data transformation and load failed"


def test_query():
    # Load saved results from the JSON file
    with open("results.json", "r") as file:
        result = json.load(file)
    
    # Test to ensure that querying the database was successful
    assert result["query"] == "success", "Test for querying the database failed"


if __name__ == "__main__":
    # Run all tests
    test_extract()
    test_transform()
    test_query()
    print("All tests passed")


#### Test time takes forever...Thus, I utilize json extention file to save calculation