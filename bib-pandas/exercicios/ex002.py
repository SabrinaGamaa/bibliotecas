#7. Crie um novo DataFrame com as seguintes informações:
import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/bib-pandas/exercicios/dataset2.csv')
print(dados.columns)
print(dados)
print('-=' * 40)
# Agrupe os dados por Departamento e calcule a soma dos salários por departamento.
teste = dados.groupby('Departamento')['Salário'].sum().reset_index()
print(teste)

