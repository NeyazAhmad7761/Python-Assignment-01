import requests


def download_file(url, file_name):
    # Send a GET request to the provided URL
    print("hi")
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
if __name__ == "__main__":
	url = 'https://example.com/file.pdf'
	file_name = 'file.pdf'
	download_file(url, file_name)