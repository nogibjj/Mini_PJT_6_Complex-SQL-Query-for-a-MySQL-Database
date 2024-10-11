# Step1

import requests

def extract(
    url="https://raw.githubusercontent.com/nogibjj/Mini_PJT_3_Polars_ISL/refs/heads/main/HR.csv",
    file_path="HR.csv",
    timeout=10
):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises an error for bad status codes
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    except (requests.exceptions.RequestException, OSError):
        return None

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

