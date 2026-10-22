import pandas as pd

def csv_to_pandas(file_name, pln):
    df = pd.read_csv('rates.csv')
    print(df)
    df['brand'] = df['brand'] * pln
    print(df)


csv_to_pandas('rates.csv', 5)
