import pandas as pd
import numpy as np

df = pd.read_csv('database/raw/netflix_users_corrected.csv')

def process_data_safe(df, churn_threshold=100):
    df = df.copy()
    
    df['Last_Login'] = pd.to_datetime(df['Last_Login'])
    max_date = df['Last_Login'].max()
    days_since_login = (max_date - df['Last_Login']).dt.days
    df['Churn'] = (days_since_login > churn_threshold).astype(int)

    df['Usage_Intensity'] = df['Watch_Time_Hours'] / (df['Age'] + 1)
    
    avg_watch = df['Watch_Time_Hours'].mean()
    df['Is_Heavy_User'] = (df['Watch_Time_Hours'] > avg_watch).astype(int)
    
    df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 35, 50, 100], labels=[0, 1, 2, 3])

    df = df.drop(columns=['User_ID', 'Name', 'Last_Login'])

    subs_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
    df['Subscription_Type'] = df['Subscription_Type'].map(subs_map)
    
    df = pd.get_dummies(df, columns=['Country', 'Favorite_Genre'], dtype=int)
    
    filename = f'database/processed/netflix_users_safe_t{churn_threshold}.csv'
    df.to_csv(filename, index=False)
    
    print(f"Dataset SEGURO: {filename}")
    print(df['Churn'].value_counts(normalize=True))
    
    return df

df_final = process_data_safe(df, churn_threshold=100)