## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):
### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 
# Demonstre tudo através de um único gráfico.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
sub_cat = dados.groupby(['Categoria','SubCategoria']).sum(numeric_only= True).sort_values('Valor_Venda', ascending=False).head(12)
print(sub_cat)
print('-=' * 60)
sub_cat = sub_cat[['Valor_Venda']].astype(int).sort_values(by= ['Categoria']).reset_index()
print(sub_cat)
print('-=' * 60)
dados_cat = sub_cat.groupby('Categoria').sum(numeric_only=True).reset_index()
print(dados_cat)

# Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

# Listas de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

# Plot
# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Gráfico das categorias
p1 = ax.pie(dados_cat['Valor_Venda'], 
            radius = 1,
            labels = dados_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(sub_cat['Valor_Venda'],
            radius = 0.9,
            labels = sub_cat['SubCategoria'],
            autopct = autopct_format(sub_cat['Valor_Venda']),
            colors = cores_subcategorias, 
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'), 
            pctdistance = 0.53,
            rotatelabels = True)

# Limpa o centro do círculo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(sub_cat['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()