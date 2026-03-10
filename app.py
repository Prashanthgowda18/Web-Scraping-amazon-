# This app scrap the product data 

#BeautifulSoup4
#requests
#lxml

from bs4 import BeautifulSoup
import requests 
import csv 

url="https://www.amazon.in/Allen-Solly-Regular-AMKP317G04249_Jet-Black_Large/dp/B06Y2FG6R7/?_encoding=UTF8&ref_=pd_hp_d_btf_crs_zg_bs_1571271031&psc=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
   # print(response.status_code)
   html_content=response.text
else:
    print("fetching error", response.status_code)

#print(html_content)
    
 #         _
#      .__(.)>
#       \___)

soup = BeautifulSoup(html_content, 'lxml')

#print(soup.prettify())

product_title = soup.find("span", id="productTitle").text.strip()  
product_price = soup.find("span", class_="a-price-whole").text.strip()
product_rating = soup.find("span",id="acrPopover").text.strip()
product_bulletPoint = soup.find("div",id="voyagerAccordian_feature_div").text.strip()
product_description = soup.find("div",id="productDescription").text.strip()
product_review = soup.find("div",class_="card-padding").text.strip()


print(product_review)

 #saving the data 

with open("amazon_product.csv", mode='w', newline='')as file:
    writer =csv.writer(file)
    writer.writerow(["product_title","product_price","product_review","product_rating","product_bulletPoint","product_description"])


    writer.writerow([product_title,product_price,product_review,product_rating,product_bulletPoint,product_description])

print("data saved!")   

