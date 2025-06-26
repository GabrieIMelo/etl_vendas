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

Faturamento por mês  
![Faturamento por Mês](imagens/faturamento-mes.png)

Produtos mais vendidos  
![Produtos mais vendidos](imagens/top-10.png)

Ticket médio por vendedor  
![Ticket médio por vendedor](imagens/ticket-medio.png)

Faturamento por categoria de produto  
![Faturamento por categoria de produto](imagens/faturamento-categoria.png)

Distribuição dos valores de venda  
![Distribuição dos valores de venda](imagens/distribuição.png)

3. Load (Carga no Banco de Dados)

Criei e populei tabelas no MySQL com os dados limpos e transformados, e escrevi consultas SQL para gerar relatórios, como:

    Total de vendas por mês

    Produtos mais vendidos

    Ticket médio por cliente

## Como Executar o Projeto

    Clone o repositório:

git clone https://github.com/GabrieIMelo/etl-vendas.git
cd etl-vendas

    Instale as dependências:

pip install -r requirements.txt

    Configure o banco de dados MySQL:

    Crie um banco e ajuste as credenciais no arquivo .env ou diretamente no código.

    Execute os scripts SQL para criar as tabelas (em sql/).

    Execute os scripts ETL:

python extract.py
python transform.py
python load.py

    (Opcional) Rode o notebook analise_vendas.ipynb para explorar os dados e visualizar os gráficos.

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