import sqlite3
import pandas as pd

con = sqlite3.connect('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/linguagem-sql.py/estudos/cap12_dsa.db')
cursor = con.cursor()

# Criar uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitario for maior que 199
query1 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""

cursor.execute(query1)
print(cursor.fetchall())

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
print('-=' * 40)
query2 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""
cursor.execute(query2)
print(cursor.fetchall())

cursor.close()
con.close()
