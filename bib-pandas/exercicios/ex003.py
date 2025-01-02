#9. Crie o seguinte DataFrame:
# Cidade: preencha com "Desconhecida".
import pandas as pd
dados = pd.read_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/bib-pandas/exercicios/dataset3.csv')
print(dados.columns)
print(dados)
print('-=' * 40)

# Substitua os valores nulos:
print(dados.isnull())
print('-=' * 40)
print(dados.fillna(0))
print('-=' * 40)

# Substitua os valores nulos:
dados['Cidade'] = dados['Cidade'].fillna('Desconhecida')
print(dados)
print('-=' * 40)

# Idade: use a média das idades.
media_idade = dados['Idade'].mean()
dados['Idade'] = dados['Idade'].fillna(media_idade)
print(dados)
print('-=' * 40)

#10. Salve o DataFrame final do exercício 9 em um arquivo chamado dados_pandas.csv.
try:
    dados.to_csv('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/bib-pandas/exercicios/dados_pandas.csv', index=False)
except:
    print('Deu erro ao salvar o arquivo')
else:
    print('Tudo certo com seu novo arquivo dados_pandas')
