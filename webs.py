import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
price = []
rating = []
description = []

for i in range(1, 5):
    url = "https://www.flipkart.com/search?q=washing+machine+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        names = i.text
        product_name.append(names)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        prices = i.text
        price.append(prices)

    Rating = box.find_all("div", class_="_3LWZlK")
    for i in Rating:
        Rating = i.text
        rating.append(Rating)

    desc = box.find_all("div", class_="fMghEO")
    for i in desc:
        desc = i.text
        description.append(desc)

df = pd.DataFrame({"Product Name": product_name, "price": price, "Rating": rating, "Description": description})
#print(df)
df.to_csv("C:/Users/dell/Desktop/webscraping/converted_files/flipd_wasmachinedata.csv")