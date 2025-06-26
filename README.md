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
<img src="imagens/faturamento-mes.png" alt="Faturamento por Mês" style="pointer-events: none;" width="600"/>

<h3>Produtos mais vendidos</h3>
<img src="imagens/top-10.png" alt="Produtos mais vendidos" style="pointer-events: none;" width="600"/>

<h3>Ticket médio por vendedor</h3>
<img src="imagens/ticket-medio.png" alt="Ticket médio por vendedor" style="pointer-events: none;" width="600"/>

<h3>Faturamento por categoria de produto</h3>
<img src="imagens/faturamento-categoria.png" alt="Faturamento por categoria de produto" style="pointer-events: none;" width="600"/>

<h3>Distribuição dos valores de venda</h3>
<img src="imagens/distribuicao.png" alt="Distribuição dos valores de venda" style="pointer-events: none;" width="600"/>


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