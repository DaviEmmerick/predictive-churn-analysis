import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt

df = pd.read_csv('database/raw/netflix_users.csv')

def process_data(df, churn_threshold=300):
    df = df.copy()
    
    df = df.drop(columns=['User_ID', 'Name'])
    df['Last_Login']  = pd.to_datetime(df['Last_Login'])

    max_date = df['Last_Login'].max()
    df['Days_Since_Last_Login'] = (max_date - df['Last_Login']).dt.days
    
    df['Churn'] = (df['Days_Since_Last_Login'] > churn_threshold).astype(int)
    
    df = df.drop(columns=['Last_Login', 'Days_Since_Last_Login'])

    subs_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
    df['Subscription_Type'] = df['Subscription_Type'].map(subs_map)
    
    df = pd.get_dummies(df, columns=['Country', 'Favorite_Genre'], dtype=int)
    
    filename = f'database/processed/netflix_users_processed_t{churn_threshold}.csv'
    df.to_csv(filename, index=False)
    
    print(f"Arquivo salvo: {filename}")
    print(f"Proporção Final usando {churn_threshold} dias:")
    print(df['Churn'].value_counts(normalize=True))
    
    return df

df_final = process_data(df, churn_threshold=300) 
print(df_final.head())