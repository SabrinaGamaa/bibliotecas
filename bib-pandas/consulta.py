import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/dataset.csv')
print(dados.columns)
print('-=' * 30)
print(dados.head(5))
print('-=' * 30)
print('Valor max e min do Valor_Venda')
print('- -' * 15)
print(dados.Valor_Venda.describe())
print('-=' * 30)
# NOVA DATAFRAME APENAS COM O INTERVALO ESCOLHIDO
dados_query = dados.query('299 < Valor_Venda < 10000')
print(dados_query.Valor_Venda.describe())
print('-=' * 30)
print('Aqui eu quero valores acima de 799 do filtro que eu já tinha feito no dados_query')
dados_query2 = dados_query.query('Valor_Venda > 799')
print(dados_query2.head())

