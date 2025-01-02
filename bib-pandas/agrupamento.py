import pandas as pd
print('''
            Esse SEGMENTO nessas REGIÕES tem essas MEDIAS DE VENDA
''')
dados = pd.read_csv('c:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(dados[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())
print('-=' * 50)
# quero 3 calculos diferentes: MEDIA, DESVIO PADRAO, CONTANGEM
print(dados[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))
print('-=' * 50)

# Filtrar o dataframe pela coluna Segmento com valores que iniciam com a letras 'CON'
print(dados.Segmento.value_counts())
print('-=' * 50)
print(dados[dados.Segmento.str.startswith('Con')].head(5))
# se eu quiser o final da palavra é so colocar andswith
