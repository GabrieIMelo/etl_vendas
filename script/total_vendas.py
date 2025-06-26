#%%
import pandas as pd

sales = pd.read_csv("sales_data.csv")

sales

#%%

total_sales = sales["Quantity_Sold"].sum()
total_sales