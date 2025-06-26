#%%
import pandas as pd

sales = pd.read_csv("sales_data.csv")
sales

# %%

for i in range(1,13):
    if i > 9:
        filtro = (sales["Sale_Date"] >= (f"2023-{i}") ) & (sales["Sale_Date"] < (f"2023-{i+1}") )
    else:
        filtro = (sales["Sale_Date"] >= (f"2023-0{i}") ) & (sales["Sale_Date"] < (f"2023-0{i+1}") )
    vendas = sales[filtro].sort_values(by="Sale_Date", ascending=True)
    vendas.to_csv(f"Vendas_Mes_{i}.csv", index=False) 
# %%

