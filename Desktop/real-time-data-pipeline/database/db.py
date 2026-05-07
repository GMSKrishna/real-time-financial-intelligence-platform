from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/realtime_pipeline"

engine = create_engine(DATABASE_URL)