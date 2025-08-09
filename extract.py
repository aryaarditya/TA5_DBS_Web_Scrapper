import requests
import pandas as pd
import re
from datetime import datetime
from bs4 import BeautifulSoup


def scrape_data(url):
    products = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.find_all("div", class_="product-details")
        for item in items:
            try:
                title = item.find("h3").get_text(strip=True)
                price_text = item.find("span", class_="price").get_text(strip=True)
                desc = item.find_all("p")
                rating = desc[0].get_text(strip=True)
                colors = desc[1].get_text(strip=True)
                size = desc[2].get_text(strip=True)
                gender = desc[3].get_text(strip=True)
                timestamp = datetime.now().isoformat()
            except (AttributeError, IndexError):
                continue

            # Simpan data mentah, JANGAN ada casting/cleaning di sini!
            products.append({
                "Title": title,
                "Price": price_text,   # Masih string, ada simbol $ dll
                "Rating": rating,      # Masih string, misal "4.5 out of 5"
                "Colors": colors,      # Masih string, misal "3 colors"
                "Size": size,          # Masih string, misal "Size: M"
                "Gender": gender,      # Masih string, misal "Gender: Man"
                "Timestamp": timestamp
            })

        return pd.DataFrame(products)

    except requests.exceptions.RequestException:
        return pd.DataFrame()
    except Exception:
        return pd.DataFrame()
