# 🚀 Sales Data ETL Pipeline with API Integration

## 📌 Overview

This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** that collects data from Google Sheets, processes it using Python, stores it in PostgreSQL, and exposes it through REST APIs using FastAPI.

The system is designed to simulate real-world data engineering workflows including **data ingestion, transformation, incremental loading, and API serving**.

---

## 🧱 Architecture

```
Google Sheets → Python ETL → PostgreSQL → FastAPI → API Consumers
```

---

## ⚙️ Features

* 📥 Data extraction from Google Sheets API
* 🧹 Data cleaning and transformation using Pandas
* 🔁 Incremental loading using timestamp-based filtering
* 🗄️ Data storage in PostgreSQL
* 🌐 REST API built with FastAPI
* ⚡ Scalable pipeline handling 10K+ records
* ⏱️ Scheduling support using Cron (optional)

---

## 🛠️ Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, SQLAlchemy, gspread
* **Database:** PostgreSQL
* **API Framework:** FastAPI
* **Tools:** Git, Linux

---

## 📂 Project Structure

```
etl-api-project/
│
├── etl/
│   ├── extract.py        # Extract data from Google Sheets
│   ├── transform.py      # Data cleaning & transformation
│   ├── load.py           # Load data into PostgreSQL
│   └── main_etl.py       # ETL pipeline runner
│
├── api/
│   └── main.py           # FastAPI application
│
├── config/
│   └── credentials.json  # Google API credentials
│
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd etl-api-project
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 📊 Google Sheets Setup

1. Create a Google Sheet named **SalesData**
2. Add columns:

```
order_id | date | customer_name | amount | status
```

3. Enable Google Sheets API
4. Download `credentials.json` and place inside `/config`
5. Share the sheet with your service account email

---

## 🗄️ Database Setup

Run the following SQL:

```
CREATE DATABASE salesdb;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    date DATE,
    customer_name TEXT,
    amount FLOAT,
    status TEXT
);
```

Update database credentials in `load.py`.

---

## ▶️ Running the Project

### Run ETL Pipeline

```
python etl/main_etl.py
```

### Run API Server

```
uvicorn api.main:app --reload
```

---

## 🌐 API Endpoints

| Endpoint       | Description      |
| -------------- | ---------------- |
| `/`            | Health check     |
| `/sales`       | Fetch sales data |
| `/sales/total` | Get total sales  |

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔁 Incremental Loading

The pipeline processes only **new records** by comparing the latest date in the database with incoming data.

---

## ⏱️ Scheduling (Optional)

Run ETL automatically using cron:

```
*/30 * * * * python /path/to/main_etl.py
```

---

## 📈 Future Improvements

* Add logging and monitoring
* Implement error handling and retry mechanisms
* Dockerize the application
* Deploy API on cloud (Render/AWS)
* Add authentication (JWT)

---

## 👨‍💻 Author

**Udit Narayan Pandey**

* GitHub: https://github.com/Uditpandey12321
* LinkedIn: pandey-udit-narayan

---
