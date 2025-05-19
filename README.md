# 📱 Flipkart Realme Smartphones Web Scraper

This Python project performs web scraping on **Flipkart** to extract data about **Realme smartphones**, organizing the results into multiple filtered Excel sheets based on price range.


## 🔍 Project Overview

- Scrapes product **titles** and **prices** of Realme phones from Flipkart (first 5 pages).
- Cleans and structures the scraped data into a **Pandas DataFrame**.
- Filters products based on various price ranges:
  - Less than ₹10,000
  - ₹10,001 – ₹19,999
  - ₹20,001 – ₹29,999
  - ₹30,000 and above
- Saves the data into separate **Excel files** for easy analysis.



## 🚀 Technologies Used

- `requests` — To fetch HTML content from the web.
- `BeautifulSoup` — For parsing and extracting data from HTML.
- `pandas` — For data manipulation and exporting to Excel.
- `time` — To add delay between page requests and prevent rate-limiting.


## 📁 Output Files

After running the script, the following Excel files are generated:

- `all_realmi_phones.xlsx` — All scraped products
- `realmi_phones_less_than_10k.xlsx`
- `realmi_phone_gtr_than_10k_less_than_20k.xlsx`
- `realmi_phone_gtr_than_20k_less_than_30k.xlsx`
- `realmi_phone_more_than_30k.xlsx`


## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flipkart-realme-scraper.git
   cd flipkart-realme-scraper

2. **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate       # On macOS/Linux
    env\Scripts\activate          # On Windows

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the scraper**
    ```bash
    python scraper.py    

## 🔒 Disclaimer

- This script is for educational purposes only.

- Flipkart’s website structure may change over time, which could break the scraper.

- Always respect a website’s robots.txt and terms of service.

## 🔍 Notes

- Flipkart may change its HTML structure, which can break the scraper. Always inspect the website and update the CSS selectors accordingly.

- The scraper includes polite delays (time.sleep(1)) to prevent overwhelming Flipkart's servers.

- If the scraper doesn't collect any data, verify that you're not getting a CAPTCHA or redirection response.


## 💡 Author
Made with ❤️ by Rishabh Dhawad
