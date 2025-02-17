import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download images
def download_images(url, folder="images"):
    # Create folder if not exists
    os.makedirs(folder, exist_ok=True)

    # Fetch webpage content
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all image tags
    img_tags = soup.find_all("img")
    
    # Filter jpg images
    img_urls = [urljoin(url, img["src"]) for img in img_tags if "src" in img.attrs and img["src"].endswith(".jpg")]

    if not img_urls:
        print("No JPG images found.")
        return
    
    print(f"Found {len(img_urls)} JPG images. Downloading...")

    for img_url in img_urls:
        try:
            img_name = os.path.join(folder, os.path.basename(img_url))
            img_data = requests.get(img_url, headers=headers).content
            with open(img_name, "wb") as f:
                f.write(img_data)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

# Example usage
website_url = "https://www.instagram.com/akg.raw/"  # Change this to the target URL
download_images(website_url)
