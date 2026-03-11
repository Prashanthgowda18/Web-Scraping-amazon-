import requests
from bs4 import BeautifulSoup

url ="https://www.flipkart.com/search?q=shirts&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

page_soup = BeautifulSoup(response.content, "html.parser")

product_class_name = "MZeksS"

products = page_soup.find_all("div", class_=product_class_name)

for product in products:
    print(product.text)