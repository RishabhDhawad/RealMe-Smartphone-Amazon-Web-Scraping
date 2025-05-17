'''
Web Scraping Project
'''
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

BASE_URL = "https://www.amazon.in/s?k=realme+mobile&page={}"

titles = []
prices = []

for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)

    response = requests.get(url, headers=HEADERS,  timeout=10)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    for product in products:
        title_tag = product.h2
        title = title_tag.text.strip() if title_tag else "No Title"


        price_tag = product.select_one("span.a-price > span.a-offscreen")
        price = price_tag.text.strip() if price_tag else "No Price"


        titles.append(title)
        prices.append(price)

    time.sleep(1)

#clean the price string to integers
def clean_price(price_str):
    try:
        price_num = price_str.replace("₹", "").replace(",","").strip()
        return int(price_num)
    except (ValueError, AttributeError): 
        return None

cleaned_prices = [clean_price(p) for p in prices]

# Creating Dataframe
df = pd.DataFrame({
    "Title": titles,
    "Price": cleaned_prices
})

#filter
df = df.dropna(subset=["Price"])
filtered_df = df[df["Price"] > 15000]


filtered_df.to_excel("realme_smartphones.xlsx", index=False)
print("Scraping complete. Data saved to realme_smartphones.xlsx")
