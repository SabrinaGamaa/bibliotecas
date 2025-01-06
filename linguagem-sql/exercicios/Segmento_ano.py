## Pergunta de Negócio 6 (Desafio Nível Baby):
### Qual o Total de Vendas Por Segmento e Por Ano?
import pandas as pd
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], dayfirst=True)
print(dados.dtypes)
dados['Ano'] = dados['Data_Pedido'].dt.year
print(dados.columns)
print('-=' * 60)
ano = dados.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum().reset_index()
print(ano)
