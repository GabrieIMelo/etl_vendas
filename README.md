## ETL de Vendas - Python, Pandas e MySQL

# Visão Geral

Este projeto simula um processo ETL (Extract, Transform, Load) completo para uma base de dados de vendas. Eu utilizei Python e Pandas para manipulação e análise de dados, e MySQL como banco de dados para armazenamento e consultas SQL. O objetivo deste projeto é demonstrar as habilidades que eu adquiri em engenharia de dados e análise de dados usando ferramentas populares do ecossistema Python.

## Tecnologias Utilizadas

    Python

    Pandas

    MySQL

    mysql-connector-python

    Matplotlib (para visualização de dados)

## Etapas do Projeto
1. Extract (Extração de Dados)

Simulei os dados de vendas em um arquivo CSV contendo: ID do produto, data da venda, vendedor, região, valor da venda, quantidade vendida, categoria do produto, custo unitário, preço unitário, tipo de cliente, desconto, método de pagamento, canal de venda e outras colunas derivadas.

2. Transform (Transformação dos Dados)

Trabalhei na limpeza dos dados (tratamento de nulos, tipos, formatação), enriquecimento (cálculo de total da venda, ticket médio, KPIs por categoria, região e cliente), e análises exploratórias com Pandas. Gerei também gráficos com Matplotlib, como:

<h3>Faturamento por mês</h3>
<img width="853" alt="faturamento-mes" src="https://github.com/user-attachments/assets/0fa653b2-3a37-4b77-9794-e8329eb3a4cc">

<h3>Produtos mais vendidos</h3>
<img width="853" alt="top-10" src="https://github.com/user-attachments/assets/78336e54-b00f-441e-ae91-219d921128c8">

<h3>Ticket médio por vendedor</h3>
<img width="853" alt="ticket-medio" src="https://github.com/user-attachments/assets/27edb082-a25b-498e-9045-cfe94f9cbc9f">

<h3>Faturamento por categoria de produto</h3>
<img width="853" alt="faturamento-categoria" src="https://github.com/user-attachments/assets/0da652b9-714d-4a43-a9cf-84a306bd4347">

<h3>Distribuição dos valores de venda</h3>
<img width="853" alt="distribuicao" src="https://github.com/user-attachments/assets/03bf18c6-1d85-4ba6-9868-cc248ef54d97">

3. Load (Carga no Banco de Dados)
abri os arquivos no MySQL com os dados limpos e transformados, e escrevi consultas SQL para gerar relatórios, como:

        Faturamento por dia do mês
        SELECT Sale_Date AS dia, SUM(Sales_Amount) AS faturamento
        FROM vendas_mes01
        GROUP BY Sale_Date;
        <img width="256" height="584" alt="Captura de tela de 2025-06-26 04-28-06" src="https://github.com/user-attachments/assets/d25b6f85-4d98-4f9a-b9ed-3d3f1e30f31b">

        Produtos mais vendidos em janeiro
        SELECT Product_Category, SUM(Quantity_Sold) AS total_vendido
        FROM vendas_mes01
        GROUP BY Product_Category
        ORDER BY total_vendido DESC;
        <img width="344" height="107" alt="Captura de tela de 2025-06-26 04-29-12" src="https://github.com/user-attachments/assets/2a185431-ef9b-4384-a05e-a3f5ba58c6c2">

       Ticket médio por vendedor
        SELECT Sales_Rep AS Vendedor, AVG(Quantity_Sold) AS ticket_medio
        FROM vendas_mes01
        GROUP BY Sales_Rep;
        <img width="294" height="127" alt="Captura de tela de 2025-06-26 04-29-53" src="https://github.com/user-attachments/assets/9f7020a2-96cc-4e95-8314-236b2cd804ac">

## Como Executar o Projeto
 Clone o repositório:

    git clone https://github.com/GabrieIMelo/etl-vendas.git
    cd etl-vendas


Instale as dependências:

    pip install -r requirements.txt


## Estrutura do Repositório

etl-vendas/

├── data/                # Dados de entrada e saída

├── graficos/            # Para vizualisar os graficos (Matplotlib)

├── scripts/             # Scripts Python (extract, transform, load)

├── sql/                 # Scripts SQL para criação e consultas

├── tabelas/             # Tabelas especificas de cada categoria de produto

├── README.md

├── requirements.txt

## Conclusão

Este projeto me permitiu aplicar conceitos fundamentais de engenharia e análise de dados, integrando Python, Pandas e MySQL em um pipeline completo e funcional. É um exemplo prático e realista de como dados brutos podem ser transformados em insights acionáveis.
