import pandas as pd

# SIMPAN KE CSV 
def load_data(df, filename="products.csv"):
    if df.empty:
        print("DataFrame kosong, tidak ada yang disimpan.")
        return False
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke file: {filename}")
    return True

# SIMPAN KE POSTGRESQL 
from sqlalchemy import create_engine

def load_to_postgres(df, db_uri, table_name="products"):
    if df.empty:
        print("DataFrame kosong, tidak ada yang dikirim ke PostgreSQL.")
        return False
    try:
        engine = create_engine(db_uri)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil dikirim ke tabel PostgreSQL: {table_name}")
        return True
    except Exception as e:
        print(f"Error PostgreSQL: {e}")
        return False

# SIMPAN KE GOOGLE SHEETS 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_to_gsheet(df, json_key, spreadsheet_name, worksheet_index=0):
    if df.empty:
        print("DataFrame kosong, tidak ada yang dikirim ke Google Sheets.")
        return False
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open(spreadsheet_name)
        sheet = spreadsheet.get_worksheet(worksheet_index)
        sheet.clear()
        sheet.insert_row(df.columns.tolist(), 1)
        sheet.append_rows(df.values.tolist())
        print("Data berhasil dikirim ke Google Sheets!")
        return True
    except Exception as e:
        print(f"Error Google Sheets: {e}")
        return False
