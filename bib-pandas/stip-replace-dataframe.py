import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(dados.columns)

print('-=' * 40)
print(dados['Data_Pedido'].head(3))
print('- -' * 30)

#Quero remover os 2 e 0 na esquerda
print(dados['Data_Pedido'].str.lstrip('20').head(3))
# como não usei o inplace = True. Valores reais ainda continuaram com 2 e o 0

print('-=' * 40)
print(dados['ID_Cliente'].head(5))
print('- -' * 30)
print('TROCAR CG PARA AX'.center(40))
print(dados['ID_Cliente'].str.replace('CG', 'AX').head(5))
