import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python upload_script.py <image_file>")
    sys.exit(1)

file_path = sys.argv[1]
url = "http://localhost:8000/convert"

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

if response.status_code == 200:
    # Get filename from header
    content_disposition = response.headers.get('Content-Disposition', '')
    if 'filename=' in content_disposition:
        filename = content_disposition.split('filename=')[1].strip('"')
    else:
        filename = 'output.tif'
    with open(filename, 'wb') as out:
        out.write(response.content)
    print(f"Saved as {filename}")
else:
    print(f"Error: {response.status_code} {response.text}")


#Yes, this is vibe-coded. But hey, it's only used in development and testing, so who cares? Plus, it saved me a few minutes.