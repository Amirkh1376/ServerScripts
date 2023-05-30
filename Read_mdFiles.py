import requests
import markdown
from bs4 import BeautifulSoup

# Raw GitHub URL of the Markdown file
url = "https://raw.githubusercontent.com/Amirkh1376/Server/main/README.md"

# Send a GET request to fetch the content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the content of the response
    content = response.text

    # Convert Markdown to HTML
    html = markdown.markdown(content)
    print(html)
else:
    print("Failed to fetch the content. Status code:", response.status_code)

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
# Get the text content without HTML tags
text = soup.get_text()
print(text)