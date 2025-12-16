import pandas as pd
from datetime import datetime as dt

df = pd.read_csv('database/raw/netflix_users.csv')
#print(df.head())
print('ETL process started...')

def process_data(df):
    df = df.drop(columns=['User_ID', 'Name']) # Dropping unnecessary columns to churn analysis
    df['Last_Login']  = pd.to_datetime(df['Last_Login'])

    max_date = df['Last_Login'].max()
    df['Days_Since_Last_Login'] = (max_date - df['Last_Login']).dt.days
    df['Churn'] = (df['Days_Since_Last_Login'] > 50).astype(int)
    df = df.drop(columns=['Last_Login', 'Days_Since_Last_Login'])

    subs_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
    df['Subscription_Type'] = df['Subscription_Type'].map(subs_map)
   
    df = pd.get_dummies(df, columns=['Country', 'Favorite_Genre'], dtype=int)
    #print(df.dtypes)
    
    df.to_csv('database/processed/netflix_users_processed.csv', index=False)
    print(f"Arquivo salvo com sucesso!")
    return df

df = process_data(df)
print(df.head())