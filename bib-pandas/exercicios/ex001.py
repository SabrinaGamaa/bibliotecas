#1. Crie um DataFrame com os seguintes dados:
import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/bib-pandas/exercicios/dataset.csv')
print(dados.columns)
print(dados)
print('-=' * 40)

#2. Usando o DataFrame do exercício anterior, filtre apenas as pessoas com idade maior que 27 anos.
print(dados[dados['Idade'] > 27])
print('-=' * 40)

#3. Adicione uma nova coluna chamada Desconto, que contém 10% do valor do salário de cada pessoa.
desconto = (dados['Salário'] * 10 / 100)
dados['Desconto'] = desconto
print(dados)
print('-=' * 40)

#4. Multiplique os salários por 1.05 (aumento de 5%) e atualize a coluna Salário com os novos valores.
dados['Salário'] = dados['Salário'] * 1.05
print(dados)
print('-=' * 40)

#5. Exiba apenas as colunas Nome e Salário.
print(dados[['Nome', 'Salário']], sep='\n')
print('-=' * 40)
#6. Ordene o DataFrame pela coluna Salário em ordem decrescente.
ordenado = dados.sort_values(by='Salário', ascending=False)
print(ordenado)
print('-=' * 40)

#8. Remova a coluna Idade do DataFrame do exercício 1.
remove_idade = dados.drop(columns='Idade')
print(remove_idade)