import pandas as pd

print("Pandas is working!")

df = pd.read_excel("D:\Excel Anu\Superstore.csv clean.xlsx")
print(df.head())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))

print(df.groupby('Month')['Sales'].sum())

print(df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False))

import matplotlib.pyplot as plt

df.groupby('Month')['Sales'].sum().plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


df.to_excel("final_data.xlsx", index=False) 
     
     


