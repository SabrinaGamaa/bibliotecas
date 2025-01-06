## Pergunta de Negócio 4:
### Quais São as 10 Cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
cidades_maior_vendas = dados.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending=False)
print(cidades_maior_vendas.head(10))
plt.figure(figsize=(16, 6))
sns.set_palette('coolwarm')
sns.barplot(data= cidades_maior_vendas.head(10),
            y = 'Valor_Venda',
            x = 'Cidade').set(title = 'As 10 CIDADES COM MAIOR TOTAL DE VENDAS')
plt.show()

