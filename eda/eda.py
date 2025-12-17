import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt

df = pd.read_csv('database/raw/netflix_users.csv')

def analyze_churn_thresholds(df_raw):
    temp_dates = pd.to_datetime(df_raw['Last_Login'])
    max_date = temp_dates.max()
    days_inactive = (max_date - temp_dates).dt.days
    
    total = len(df_raw)
    thresholds = [30, 50, 60, 90, 120, 180]
    
    for dias in thresholds:
        churn_count = len(days_inactive[days_inactive > dias])
        perc = (churn_count / total) * 100
        status = "CRÍTICO (Desbalanceado)" if perc > 70 or perc < 10 else "OK"
        print(f"Régua > {dias} dias sem logar: {perc:.1f}% seria Churn [{status}]")

    try:
        plt.figure(figsize=(10, 5))
        sns.histplot(days_inactive, bins=50, kde=True)
        plt.title('Distribuição: Há quantos dias o usuário não loga?')
        plt.xlabel('Dias Inativo')
        plt.axvline(x=50, color='red', linestyle='--')
        plt.show()
    except:
        pass

def analyze_subscription_correlation(df_raw):
    
    df_temp = df_raw.copy()
    df_temp['Last_Login'] = pd.to_datetime(df_temp['Last_Login'])
    max_date = df_temp['Last_Login'].max()
    df_temp['Days_Since_Login'] = (max_date - df_temp['Last_Login']).dt.days

    subs_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
    df_temp['Subscription_Score'] = df_temp['Subscription_Type'].map(subs_map)

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Subscription_Type', y='Days_Since_Login', data=df_temp, 
                order=['Basic', 'Standard', 'Premium'], palette='viridis')
    plt.title("Comportamento de Login por Tipo de Assinatura")
    plt.ylabel("Dias desde o último login")
    plt.xlabel("Tipo de Assinatura")
    plt.grid(True, alpha=0.3)
    plt.show()

    plt.figure(figsize=(6, 5))
    cols_to_check = ['Subscription_Score', 'Days_Since_Login']
    corr_matrix = df_temp[cols_to_check].corr(method='spearman')
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlação: Pagar Mais vs Tempo Sem Logar")
    plt.show()
    
    corr_value = corr_matrix.loc['Subscription_Score', 'Days_Since_Login']
    print(f"Coeficiente de Correlação (Spearman): {corr_value:.4f}")
    if abs(corr_value) < 0.1:
        print("-> CONCLUSÃO: Nenhuma correlação relevante (Variável provavelmente inútil).")
    elif corr_value < 0:
        print("-> CONCLUSÃO: Correlação Negativa (Quem paga mais, fica MENOS dias sem logar). Bom sinal!")
    else:
        print("-> CONCLUSÃO: Correlação Positiva (Quem paga mais, demora MAIS para logar). Estranho...")

analyze_churn_thresholds(df)
analyze_subscription_correlation(df) 