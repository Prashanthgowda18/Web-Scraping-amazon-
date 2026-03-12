from bs4 import BeautifulSoup
import requests

url="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

containers = soup.find_all("div", {"class": "ZFwe0M row"})

product_name = containers[0].find("div", {"class": "RG5Slk"}).text

product_review_rating = containers[0].find("div", {"class": "a7saXW"}).text

print(product_review_rating)