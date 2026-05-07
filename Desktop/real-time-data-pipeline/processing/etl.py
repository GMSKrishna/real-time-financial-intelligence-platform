import pandas as pd
from database.db import engine

def extract_data():
    query = "SELECT * FROM raw_data"
    df = pd.read_sql(query, engine)

    print("Raw data extracted")
    return df

def transform_data(df):

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert price column to float
    df['price'] = df['price'].astype(float)

    # Calculate price change %
    df['price_change_percent'] = (
        df['price']
        .pct_change()
        .replace([float('inf'), -float('inf')], 0)
        .fillna(0)
        * 100
    )

# Limit unrealistic spikes
    df['price_change_percent'] = (
        df['price_change_percent']
        .clip(-100, 100)
    )

    print("Data transformed")
    return df

def load_processed_data(df):

    df.to_sql(
        "processed_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Processed data stored")

if __name__ == "__main__":

    raw_df = extract_data()

    processed_df = transform_data(raw_df)

    load_processed_data(processed_df)

    print("ETL pipeline completed successfully")