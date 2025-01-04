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

# Calcula a média dos valores
# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
media = cursor.fetchall()
print('MÉDIA DE UNIDADES VENDIDAS')
print(media)
print('-=' * 40)

# Calcula a média dos valores
# Cria uma instrução SQL para calcular a média de unidades vendidas
query7 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_produto'
cursor.execute(query7)
media = cursor.fetchall()
print('MÉDIA DE UNIDADES VENDIDAS DO grupo Nome_Produto')
print(media)
print('-=' * 40)

#Conta o número de registros.
query3 = 'SELECT COUNT(ID_Cliente) FROM tb_vendas_dsa'
cursor.execute(query3)
contador = cursor.fetchall()
print('Quando ID_ de Cliente temos: ')
print(contador)
print('-=' * 40)

# Soma os valores de uma coluna.
query4 = 'SELECT SUM(Custo) FROM tb_vendas_dsa'
cursor.execute(query4)
soma = cursor.fetchall()
print('A soma do custo é: ')
print(soma)
print('-=' * 40)

# Retorna o menor valor.
query5 = 'SELECT MIN(Custo) FROM tb_vendas_dsa'
cursor.execute(query5)
min = cursor.fetchall()
print('O valor minimo do custo é: ')
print(min)
print('-=' * 40)

# Retorna o maior valor.
query6 = 'SELECT MAX(Custo) FROM tb_vendas_dsa'
cursor.execute(query6)
max = cursor.fetchall()
print('O valor maximo do custo é: ')
print(max)
print('-=' * 40)

cursor.close()
con.close()