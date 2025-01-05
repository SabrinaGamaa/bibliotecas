## Pergunta de Negócio 2:
### Qual o Total de Vendas Por Data do Pedido?
# Demonstre o resultado através de um gráfico de barras.
import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
plt.figure(figsize=(20, 6))
total_venda = dados.groupby('Data_Pedido')['Valor_Venda'].sum()
grafico = total_venda.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
plt.title('Total de Vendas Por DATA DO PEDIDO')
plt.show()

