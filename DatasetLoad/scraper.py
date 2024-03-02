# import os
# import requests
# from bs4 import BeautifulSoup
# import urllib
# from tqdm import tqdm

# # Function to download image given a URL
# def download_image(url, filename, folder):
#     # Create the folder if it doesn't exist
#     os.makedirs(folder, exist_ok=True)
#     filepath = os.path.join(folder, filename)
#     urllib.request.urlretrieve(url, filepath)

# # Base URL of the page to scrape
# base_url = "https://tma.im/cgi-bin/selectImages.pl?diagnosis=lymphoma"
# current_page_url = base_url

# # Loop to navigate through pages
# while current_page_url:
#     # Send a GET request to the current page URL
#     response = requests.get(current_page_url)

#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all image links
#     image_links = soup.find_all('a', href=lambda href: (href and href.endswith('.jpg')))

#     # Download each image
#     for link in tqdm(image_links):
#         image_url = 'https://tma.im' + link['href']  # Construct absolute URL
#         filename = link['href'].split('/')[-1]  # Extract filename from the URL
#         download_image(image_url, filename, "archive1")  # Pass the folder name as argument
#         print(f"Downloaded: {filename}")

#     # Find the link to the next page
#     next_page_link = soup.find('a', text='Next Page')
#     if next_page_link:
#         current_page_url = 'https://tma.im' + next_page_link['href']  # Construct absolute URL
#     else:
#         current_page_url = None  # If there is no next page, stop the loop


import os
import requests
from bs4 import BeautifulSoup
import urllib
from tqdm import tqdm

# Function to download image given a URL
def download_image(url, filename, folder):
    # Create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    urllib.request.urlretrieve(url, filepath)

# Base URL of the page to scrape
# base_url = "https://tma.im/cgi-bin/selectImages.pl?diagnosis=lymphoma"
# base_url = "https://tma.im/cgi-bin/viewStain.pl?stain_no=3241&view=Printable"
# base_url = "https://tma.im/cgi-bin/viewStain.pl?stain_no=3742&view=Printable"
# base_url = "https://tma.im/cgi-bin/viewStain.pl?stain_no=3601&view=Printable"
base_url = "https://tma.im/cgi-bin/viewStain.pl?stain_no=2832&view=Printable"
current_page_url = base_url

# Session object to persist cookies across requests
session = requests.Session()
# Submit the form
# response = session.post(base_url, data={"250 small images": "250 small images"})
response = requests.get(current_page_url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image links
image_links = soup.find_all('a', href=lambda href: (href and href.endswith('.jpg')))

# Download each image
for link in tqdm(image_links):
    image_url = 'https://tma.im' + link['href']  # Construct absolute URL
    filename = link['href'].split('/')[-1]  # Extract filename from the URL
    download_image(image_url, filename, "npImages")  # Pass the folder name as argument
    tqdm.write(f"Downloaded: {filename}")
