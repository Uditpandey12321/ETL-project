from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    dbname="salesdb",
    user="postgres",
    password="password",
    host="localhost"
)

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/sales")
def get_sales():
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales LIMIT 50")
    data = cur.fetchall()
    return {"data": data}

@app.get("/sales/total")
def total_sales():
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM sales")
    total = cur.fetchone()
    return {"total_sales": total[0]}
