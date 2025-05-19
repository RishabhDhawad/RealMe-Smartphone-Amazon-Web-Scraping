'''
Web Scraping Project
'''
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com"
}

BASE_URL = "https://www.flipkart.com/mobiles/realme~brand/pr?sid=tyy%2C4io&page={}"

titles = []
prices = []

for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("div", class_="tUxRFH")
    print(f"Found {len(products)} products on page {page}")

    for product in products:
        title_tag = product.find("div", class_="KzDlHZ")
        title = title_tag.text.strip() if title_tag else "No Title"

        price_tag = product.find("div", class_="Nx9bqj _4b5DiR")
        price = price_tag.text.strip() if price_tag else "No Price"

        titles.append(title)
        prices.append(price)

    time.sleep(1)

#clean the price string
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

# filter phones less than 10k
df_less_than_10k = df[df["Price"] < 10000]

# filter phone greater than 10,000 less than 20,000 rupees
df_gtr_than_10k_less_than_20k = df[(df["Price"] > 10000) & (df["Price"] < 20000)]

# filter phone greater than 20,000 less than 30,000 rupees
df_gtr_than_20k_less_than_30k = df[(df["Price"] > 20000) & (df["Price"] < 30000)] 

# filter phones more than 30k
df_more_than_30k = df[df["Price"] > 30000]


# GENERAL PRINT STATEMENT
print(f"Titles collected: {len(titles)}")
print(f"Prices collected: {len(prices)}")


# without any filter
df.to_excel("all_realmi_phones.xlsx", index=False)
print("Scraping complete. Data saved to all_realmi_phones.xlsx")

# filter phones less than 10k
df_less_than_10k.to_excel("realmi_phones_less_than_10k.xlsx", index=False)
print("Scraping complete. Data saved to realmi_phones_less_than_10k.xlsx")

# filter phone greater than 10,000 less than 20,000 rUpees
df_gtr_than_10k_less_than_20k.to_excel("realmi_phone_gtr_than_10k_less_than_20k.xlsx", index=False)
print("Scraping complete. Data saved to realmi_phone_gtr_than_10k_less_than_20k.xlsx")

# filter phone greater than 20,000 less than 30,000 rupees
df_gtr_than_20k_less_than_30k.to_excel("realmi_phone_gtr_than_20k_less_than_30k.xlsx", index=False)
print("Scraping complete. Data saved to realmi_phone_gtr_than_20k_less_than_30k.xlsx")

# filter phones more than 30k
df_more_than_30k.to_excel("realmi_phone_more_than_30k.xlsx", index=False)
print("Scraping complete. Data saved to realmi_phone_more_than_30k.xlsx")
