import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(f' O arquivo tem linhas, colunas: {dados.shape}')
print('-=' * 30)
print(f'Agora vai mostrar somente as quantidades que tem 5, 7, 9: ')
print(f'O arquivo tem linhas, colunas: {dados[dados['Quantidade'].isin([5, 7, 9])].shape}')
print('-=' * 30)
print('Agora quero as 10 primeiras linhas das quantidades filtradas 5, 7, 9:')
print(dados[dados['Quantidade'].isin([5, 7, 9])][:10])
