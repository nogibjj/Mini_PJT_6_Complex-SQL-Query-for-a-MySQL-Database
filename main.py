import json
from mylib.extract import extract
from mylib.transform import load_data_to_db
from mylib.query import run_query

# Main function to handle 3 key processes: Extract, Transform & Load, and Query
def main_res():
    print("Extracting data...")
    extract_result = extract()

    print("Transforming and loading data to database...")
    transform_result = load_data_to_db()

    print("Querying the database...")
    query_result = run_query()

    # Store results in a dictionary
    results = {
        "extract": extract_result,
        "transform_db": transform_result,
        "query": query_result,
    }

    return results


if __name__ == "__main__":
    # Call the main function and get the results
    final_results = main_res()

    # Print the final results for each process
    print(f"Results: {final_results}")

    # Save results to a JSON file for testing, specifying UTF-8 encoding
    with open("results.json", "w", encoding="utf-8") as file:  # Encoding specified here
        json.dump(final_results, file)
