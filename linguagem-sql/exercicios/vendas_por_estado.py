## Pergunta de Negócio 3:
### Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras.
import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
total_estado = dados.groupby('Estado')['Valor_Venda'].sum().sort_index(ascending=True)
print(total_estado.head(5))
plt.figure(figsize=(16, 6))
total_estado.plot.bar(x = 'Estado', y = 'Valor_Venda', color = 'blue')
plt.title('TOTAL DE VENDAS POR ESTADO')
plt.show()
