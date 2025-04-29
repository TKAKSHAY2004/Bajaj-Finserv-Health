import requests

# Define the API endpoint
url = "http://127.0.0.1:8000/lab_reports_samples"

# Path to the image file you want to upload
file_path = "lab_reports_samples/lbmaske/AHD-0425-PA-0007719_E-REPORTS_250427_2032@E.pdf_page_4.png"  # Update with your file path

# Open the file in binary mode and send it to the API
with open(file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

# Print the response from the API
print(response.json())