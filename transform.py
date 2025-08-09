EXCHANGE_RATE = 16000

dirty_patterns = {
    "Title": ["Unknown Product"],
    "Rating": ["Invalid Rating / 5", "Not Rated"],
    "Price": ["Price Unavailable", None],
}

def transform_data(df):
    if df.empty:
        return df
    # Drop invalid data, hapus NaN, dsb
    df = df.drop_duplicates().dropna()
    
    # Clean kolom Price: buang $, koma, konversi ke float lalu kalikan kurs
    df["Price"] = df["Price"].str.replace("[$,]", "", regex=True).astype(float) * EXCHANGE_RATE
    
    # Clean kolom Rating: ambil angka saja
    df["Rating"] = df["Rating"].str.extract(r"(\d+(\.\d+)?)")[0].astype(float)
    
    # Clean Colors: ambil angka saja, kalau tidak ada 0
    df["Colors"] = df["Colors"].str.extract(r"(\d+)")[0].fillna(0).astype(int)
    
    # Clean Size dan Gender
    df["Size"] = df["Size"].str.replace("Size:", "", regex=False).str.strip()
    df["Gender"] = df["Gender"].str.replace("Gender:", "", regex=False).str.strip()
    
    # Drop row yang tidak valid (jika perlu)
    df = df[~df["Title"].isin(dirty_patterns["Title"])]
    df = df[~df["Price"].isnull()]
    df = df[~df["Rating"].isnull()]
    
    return df
