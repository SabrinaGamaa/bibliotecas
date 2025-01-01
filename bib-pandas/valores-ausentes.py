import pandas as pd
dsa_df = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
pd.set_option('display.max_columns', None)
print(dsa_df.columns)
print(dsa_df.head())
# Quero chamar os valores ausentes e somar
print('-=' * 20)
print(dsa_df.isna().sum())
print('-=' * 20)
# Extraimos a moda da coluna quantidade que tem dois valares ausentes e a moda vai ver os valores mais comuns da quantidade
moda = dsa_df['Quantidade'].value_counts().index[0]
# Entrao qual é o numero que aparece mais vezes na 'Quantidade'
print(moda)
print('-=' * 20)
# ESSE: dsa_df.fillna({'Quantidade': moda}, inplace=True)
dsa_df['Quantidade'] = dsa_df['Quantidade'].fillna(moda)
print(dsa_df.isna().sum())

