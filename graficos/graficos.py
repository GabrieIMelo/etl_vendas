# %%
import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv("sales_data.csv")
sales

# %%
# Converter datas
sales['Sale_Date'] = pd.to_datetime(sales['Sale_Date'])
sales['Month'] = sales['Sale_Date'].dt.to_period('M')
# Agrupar faturamento por mês
faturamento_mensal = sales.groupby('Month')['Sales_Amount'].sum()
# Plotar
faturamento_mensal.plot(kind='bar', title='Faturamento por Mês', figsize=(10, 4))
plt.ylabel('Total em vendas (R$)')
plt.xlabel('Mês')
plt.tight_layout()
plt.show()

#%%
top_produtos = sales.groupby('Product_ID')['Quantity_Sold'].sum().sort_values(ascending=False).head(10)

top_produtos.plot(kind='barh', title='Top 10 Produtos Mais Vendidos', figsize=(8, 5))
plt.xlabel('Quantidade Vendida')
plt.ylabel('ID do Produto')
plt.tight_layout()
plt.show()
# %%
ticket_medio_rep = sales.groupby('Sales_Rep')['Sales_Amount'].mean().sort_values()

ticket_medio_rep.plot(kind='bar', title='Ticket Médio por Vendedor', figsize=(8, 4))
plt.ylabel('Ticket Médio (R$)')
plt.xlabel('Vendedor')
plt.tight_layout()
plt.show()
# %%
categoria_vendas = sales.groupby('Product_Category')['Sales_Amount'].sum().sort_values()

categoria_vendas.plot(kind='bar', title='Faturamento por Categoria de Produto', figsize=(7, 4))
plt.ylabel('Faturamento (R$)')
plt.xlabel('Categoria')
plt.tight_layout()
plt.show()

# %%
sales['Sales_Amount'].plot(kind='hist', bins=20, title='Distribuição dos Valores de Venda', figsize=(8, 4))
plt.xlabel('Valor da Venda (R$)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()
# %%
