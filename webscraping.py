import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

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

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"⚠️ Failed to fetch page {page}")
        continue

    soup = BeautifulSoup(response.content, "lxml")
    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    for product in products:
        title_tag = product.find("span")
        price_tag = product.select_one("span.a-price > span.a-offscreen")

        title = title_tag.text.strip() if title_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"

        titles.append(title)
        prices.append(price)

    time.sleep(1)  # polite delay to avoid getting blocked

# Save to Excel
df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})
df.to_excel("realme_smartphones.xlsx", index=False)
print("✅ Scraping complete. Data saved to realme_smartphones.xlsx")
