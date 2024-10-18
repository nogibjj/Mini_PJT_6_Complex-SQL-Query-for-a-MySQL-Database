# Step1

import requests

def extract(
    url1="https://raw.githubusercontent.com/nogibjj/Mini_PJT_6_Complex-SQL-Query-for-a-MySQL-Database/refs/heads/main/data_raw/HR_1.csv",
    file_path1="data/HR_1.csv",
    url2="https://raw.githubusercontent.com/nogibjj/Mini_PJT_6_Complex-SQL-Query-for-a-MySQL-Database/refs/heads/main/data_raw/HR_2.csv",
    file_path2="data/HR_2.csv",
    timeout=10
):
    try:
        # Download and save the first CSV file
        response1 = requests.get(url1, timeout=timeout)
        response1.raise_for_status()  # Raises an error for bad status codes
        with open(file_path1, "wb") as f1:
            f1.write(response1.content)
        print(f"Downloaded and saved: {file_path1}")
        
        # Download and save the second CSV file
        response2 = requests.get(url2, timeout=timeout)
        response2.raise_for_status()  # Raises an error for bad status codes
        with open(file_path2, "wb") as f2:
            f2.write(response2.content)
        print(f"Downloaded and saved: {file_path2}")
        
        return file_path1, file_path2
    except (requests.exceptions.RequestException, OSError) as e:
        print(f"An error occurred: {e}")
        return None, None

if __name__ == "__main__":
    extract()



# def extract(
#     url="https://raw.githubusercontent.com/nogibjj/Mini_PJT_3_Polars_ISL/refs/heads/main/HR.csv",
#     file_path="HR.csv",  # Save directly in the current directory
#     timeout=10  # Set a timeout value in seconds
# ):

#     # Download the file
#     try:
#         response = requests.get(url, timeout=timeout)  # Add the timeout parameter
#         if response.status_code == 200:
#             with open(file_path, "wb") as f:
#                 f.write(response.content)
#             print(f"File downloaded and saved to {file_path}")
#         else:
#             print(f"Failed to download the file. Status code: {response.status_code}")
#     except requests.exceptions.Timeout:
#         print(f"Request timed out after {timeout} seconds.")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

#     return file_path


# if __name__ == "__main__":
#     extract()

