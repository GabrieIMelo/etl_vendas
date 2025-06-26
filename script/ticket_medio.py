#%%
import pandas as pd

sales = pd.read_csv("sales_data.csv")
sales

#%%

total_sales = sales["Quantity_Sold"].sum()
total_sales

#%%

total_amount = sales["Sales_Amount"].sum()
total_amount

#%%

ticket_medio = total_amount / total_sales
ticket_medio
