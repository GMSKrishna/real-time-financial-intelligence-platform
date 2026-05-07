import requests
import pandas as pd
from datetime import datetime
from database.db import engine

def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    df['timestamp'] = datetime.now()

    return df

def store_raw_data(df):
    df.to_sql("raw_data", engine, if_exists="append", index=False)
    print("Data stored successfully!")

if __name__ == "__main__":
    df = fetch_crypto_data()
    store_raw_data(df)