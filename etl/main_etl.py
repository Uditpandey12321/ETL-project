from extract import extract_data
from transform import transform_data
from load import load_data, get_last_date

def run_etl():
    df = extract_data()

    last_date = get_last_date()

    if last_date:
        df = df[df['date'] > last_date]

    df = transform_data(df)

    if not df.empty:
        load_data(df)
        print("Data loaded successfully")
    else:
        print("No new data")

if __name__ == "__main__":
    run_etl()
