import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(dados['ID_Pedido'].head(5))
print('-=' * 50)

print(dados['ID_Pedido'].str.split('-').head(5))
print('-=' * 50)

print('Quero ID_Pedido o ANO')
print(dados['ID_Pedido'].str.split('-').str[1].head(5))
print('-=' * 50)

print('FAZENDO O SPLIT DA COLUNA E EXTRAIMOS O ITEM NA POSIÇÃO 2')
dados['Ano'] = dados['ID_Pedido'].str.split('-').str[1]
pd.set_option('display.max_columns', None)
print(dados.head(10))
