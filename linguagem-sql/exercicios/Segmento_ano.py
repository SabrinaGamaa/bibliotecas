## Pergunta de Negócio 6 (Desafio Nível Baby):
### Qual o Total de Vendas Por Segmento e Por Ano?
import pandas as pd
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
ano = dados[dados['Data_Pedido'] in '/20']
print(ano)

