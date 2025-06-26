#%% 
import pandas as pd

sales = pd.read_csv("sales_data.csv")
sales

#%%
filtro = sales["Product_Category"] == "Furniture"
sales[filtro].to_csv("Tabela_Furniture.csv", index=False)
# %%
filtro = sales["Product_Category"] == "Food"
sales[filtro].to_csv("Tabela_Food.csv", index=False)
# %%
filtro = sales["Product_Category"] == "Eletronics"
sales[filtro].to_csv("Tabela_Eletronics.csv", index=False)
#%%
filtro = sales["Product_Category"] == "Clothing"
sales[filtro].to_csv("Tabela_Clothing.csv", index=False)
# %%

fur = pd.read_csv("Tabela_Furniture.csv")
fur
#%%
fur.sort_values(by=["Sales_Amount"], ascending=[False]).head(10)
# %%

