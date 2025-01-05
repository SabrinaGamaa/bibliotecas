import sqlite3
import pandas as pd

con = sqlite3.connect('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/linguagem-sql/estudos/cap12_dsa.db')
cursor = con.cursor()

query = 'SELECT * FROM tb_vendas_dsa'

cursor.execute(query)
dados = cursor.fetchall()

print(dados[:10])
print('-=' * 60)

# lista = pd.read_sql_query('SELECT * FROM tb_vendas_dsa', con)
# print(lista.head(10))

# media = lista['Unidades_Vendidas'].mean()
# print(media)


df = pd.DataFrame(dados, columns=['ID_Pedido',
                                     'ID_Cliente',
                                     'Nome_Produto',
                                     'Valor_Unitario',
                                     'Unidades_Vendidas',
                                     'Custo'])
print(df.head(10))

print('--' * 60)
media_das_unidades = df['Unidades_Vendidas'].mean()
print(f'Media das Unidades Vendidas: {media_das_unidades}')
print('--' * 60)
media_das_unidades_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(f'Media das Unidades Vendidas por Produto: \n{media_das_unidades_por_produto.head(10)}')
print('--' * 60)
# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
print('Média de unidades vendidas por produto se o valor unitario for maior do que 199.')
media_das_unidades_maior_199 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(media_das_unidades_maior_199)
print('--' * 60)

# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.
print('OPÇÃO 1: Média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.')
op1 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
print(op1)
print('--' * 60)
print('OPÇÃO 2:')
op2 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                                    .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                                    .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(op2)

cursor.close()
con.close()

