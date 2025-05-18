# 📱 Flipkart Realme Smartphones Web Scraper

This project is a Python-based web scraper that extracts data about Realme smartphones listed on Flipkart. The scraper collects product titles and prices, filters smartphones above ₹15,000, and exports the data to an Excel file for further analysis.

---

## 🛠 Features

- Scrapes multiple pages of Realme smartphones on Flipkart
- Extracts product titles and prices
- Cleans and converts prices into integers
- Filters products priced above ₹15,000
- Saves the cleaned data into an Excel file (`realme_smartphones.xlsx`)

---

## 🧰 Tech Stack

- Python 🐍
- BeautifulSoup (HTML parsing)
- Requests (HTTP requests)
- pandas (data manipulation)
- openpyxl (Excel file support)

---

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

3 **Install dependencies**

    pip install -r requirements.txt

4 **Run the scraper**

    python scraper.py

## 📂 Output
The script generates a file named:
    
    realme_smartphones.xlsx

This file will contain the list of Realme smartphones whose prices are above ₹15,000, along with their titles.

## 🔍 Notes

- Flipkart may change its HTML structure, which can break the scraper. Always inspect the website and update the CSS selectors accordingly.

- The scraper includes polite delays (time.sleep(1)) to prevent overwhelming Flipkart's servers.

- If the scraper doesn't collect any data, verify that you're not getting a CAPTCHA or redirection response.

## 📸 Screenshots

| Titles Extracted | Prices Extracted |
|------------------|------------------|
| realme Narzo 60X 5G (Green) | ₹15,999          |
| realme 11X 5G (Purple)       | ₹16,999          |
| realme 12 Pro+ 5G (Blue)      | ₹28,999          |

## 📌 License
This project is licensed under the MIT License. Feel free to fork, modify, and use it as needed.

## 💡 Author
Made with ❤️ by Rishabh Dhawad