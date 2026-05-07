from fastapi import FastAPI
import pandas as pd
from database.db import engine

app = FastAPI(
    title="Real-Time Financial Intelligence API",
    description="Real-time crypto analytics backend",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "API is running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/latest-data")
def latest_data():

    query = """
    SELECT *
    FROM processed_data
    ORDER BY timestamp DESC
    LIMIT 20
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

@app.get("/top-movers")
def top_movers():

    query = """
    SELECT *
    FROM processed_data
    ORDER BY price_change_percent DESC
    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")