from sqlalchemy import create_engine
import pandas as pd

DB_URL = "postgresql://postgres:password@localhost:5432/salesdb"
engine = create_engine(DB_URL)

def load_data(df):
    df.to_sql("sales", engine, if_exists="append", index=False)

def get_last_date():
    query = "SELECT MAX(date) FROM sales"
    try:
        last_date = pd.read_sql(query, engine).iloc[0, 0]
        return last_date
    except:
        return None
