import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(dados.columns)
print('-=' * 40)

print('Criando uma nova vareavel. Com a combinação de ID_pedido e Segmento.'.center(40).upper())
# Vou criar Pedido Segmento que vai receber ID_Pedido e Segmento com a função CAT e SEP que vai separar por '-'
dados['Pedido_Segmento'] = dados['ID_Pedido'].str.cat(dados['Segmento'], sep='-')
print(dados.columns)
print('-=' * 40)
print(dados[['ID_Pedido', 'Segmento']].head(5))
print('- -' * 30)
print(dados['Pedido_Segmento'].head(5))
