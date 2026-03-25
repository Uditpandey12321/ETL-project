def transform_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna({"amount": 0}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df['customer_name'] = df['customer_name'].str.title()
    return df
