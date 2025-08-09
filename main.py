from utils.extract import scrape_data
from utils.transform import transform_data
from utils.load import load_data, load_to_postgres, load_to_gsheet

# Konfigurasi 
BASE_URL = "https://fashion-studio.dicoding.dev/"
CSV_FILENAME = "products.csv"
POSTGRES_DB_URI = "postgresql+psycopg2://postgres:dtsx@localhost:5432/product"
JSON_KEY = r"C:\Users\ACER\OneDrive\Documents\DBS Coding Camp\Tugas\TA 5\google-sheets-api.json"
SPREADSHEET_NAME = "products"
MAX_PAGES = 50


# EXTRACT 
def scrape_all_pages(max_pages=50):
    import pandas as pd
    all_products = pd.DataFrame()
    print("\nScraping page 1...")
    df = scrape_data(BASE_URL)
    all_products = pd.concat([all_products, df], ignore_index=True)
    for page in range(2, max_pages + 1):
        print(f"\nScraping page {page}...")
        page_url = f"{BASE_URL}page{page}"
        df = scrape_data(page_url)
        if df.empty:
            print("No more data found, stopping pagination.")
            break
        all_products = pd.concat([all_products, df], ignore_index=True)
    return all_products

# ETL PIPELINE 
if __name__ == "__main__":
    # 1. Extract
    data = scrape_all_pages(MAX_PAGES)
    print(f"\nJumlah data hasil scraping: {len(data)}")

    # 2. Transform
    cleaned_data = transform_data(data)
    print(f"\nJumlah data setelah transformasi: {len(cleaned_data)}")

    # 3. Preview
    if not cleaned_data.empty:
        from tabulate import tabulate
        preview_df = cleaned_data.head().copy()
        preview_df["Price"] = preview_df["Price"].apply(lambda x: f"{x:,.0f}")
        print("\nPreview data hasil akhir:")
        print(tabulate(preview_df, headers='keys', tablefmt='github', showindex=True))
        print("\nStruktur DataFrame setelah transformasi:")
        cleaned_data.info()
    else:
        print("Tidak ada data yang berhasil diproses!")

    # 4. Load: CSV
    load_data(cleaned_data, CSV_FILENAME)

    # 5. Load: PostgreSQL
    load_to_postgres(cleaned_data, POSTGRES_DB_URI, table_name="products")

    # 6. Load: Google Sheets
    load_to_gsheet(cleaned_data, JSON_KEY, SPREADSHEET_NAME)

