import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
data = load_iris()
import pandas as pd
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']
print(df.head(5))
# faz os dados do grafico
df.plot()
# me mostra o grafico
plt.show()

# mostrar os dados de duas colunas
df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')
plt.show()

# mostrar dados das colunas escolhidas background
colunas = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[colunas].plot.area()
plt.show()

# vou agrupar as colunas species e criar um grafico de barras
df.groupby('species').mean().plot.bar()
plt.show()

# grafico contagem em grafico de pizza
df.groupby('species').count().plot.pie(y = 'sepal length (cm)')
plt.show()

#Grafico KDE
df.plot.kde(subplots= True, figsize = (8, 8))
plt.show()

#boxplot de cada variavel numerica
colunas2 = ['sepal length (cm)', 'sepal width (cm)', 'petal width (cm)', 'petal length (cm)']
df[colunas2].plot.box(figsize = (8, 8))
plt.show()
