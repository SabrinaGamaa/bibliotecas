import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
pd.set_option('display.max_columns', 11)
# Filtrando para HOME OFFICE e REGIAO
print(dados[(dados.Segmento == 'Home Office') & (dados.Regiao == 'South')].head(5))
print('-=' * 70)
# Filtrando para HOME OFFICE OU REGIAO
# tail são os ultimos
print(dados[(dados.Segmento == 'Home Office') | (dados.Regiao == 'South')].tail(5))
print('-=' * 70)
# Filtrando os que não ocorrem em home office e nem a regial South
# sample é amostra ele vai mostra os 5 resultado que pedi
print(dados[(dados.Segmento != 'Home Office') & (dados.Regiao != 'South')].sample(5))

