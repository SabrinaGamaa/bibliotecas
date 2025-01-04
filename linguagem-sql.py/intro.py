import sqlite3
import pandas as pd

con = sqlite3.connect('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/linguagem-sql.py/estudos/cap12_dsa.db')
cursor = con.cursor()

# Listar todas as tabelas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
print('Tabelas no banco de dados:')
print(cursor.fetchall())
print('-=' * 40)

# Acessar a tabela tb_vendas_dsa
query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)

# Obter nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]
print('Nomes das colunas: ')
print(nomes_colunas)
print('-=' * 40)

# Obter dados da tabela
dados = cursor.fetchall()
print('Dados da TABELA até os 10 primeiros: ')
print(dados[:10])
print('-=' * 40)

# Usar Pandas para carregar os dados diretamente no DataFrame
df = pd.read_sql_query('SELECT * FROM tb_vendas_dsa', con)
print('Dados em formado DATAFRAME:')
print(df.head(5))

cursor.close()
con.close()
