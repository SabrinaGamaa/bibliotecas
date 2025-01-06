## Pergunta de Negócio 9 (Desafio Nível Master Ninja):
### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# Demonstre o resultado através de gráfico de linha.

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
segmento = dados.groupby('Segmento')['Valor_Venda']
print(segmento.mean().reset_index())
print('-=' * 60)
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], dayfirst=True)
dados['Ano'] = dados['Data_Pedido'].dt.year
dados['Mes'] = dados['Data_Pedido'].dt.month
media_ano = dados.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
print('A media de vendas por Segmento, por ano e por mes.')
print(media_ano)
anos = media_ano.index.get_level_values(0)
mes = media_ano.index.get_level_values(1)
seg = media_ano.index.get_level_values(2)

plt.figure(figsize=(12, 6))
sns.set()
fig1 = sns.relplot(kind= 'line',
                   data= media_ano,
                   y= 'mean',
                   x= mes,
                   hue= seg,
                   col= anos,
                   col_wrap= 4)
plt.show()

