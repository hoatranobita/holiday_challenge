import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/telco-customer-churn-by-IBM.csv')
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df['SeniorCitizen'] = df['SeniorCitizen'].astype(str)