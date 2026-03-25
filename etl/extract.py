import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

def extract_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(
        "config/credentials.json", scopes=scope
    )

    client = gspread.authorize(creds)
    sheet = client.open("SalesData").sheet1

    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    return df
