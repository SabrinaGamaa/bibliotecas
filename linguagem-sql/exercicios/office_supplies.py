import pandas as pd
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
print(dados.head(5))
print('-=' * 60)

## Pergunta de Negócio 1:
### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
office_supplies = dados[dados['Categoria'] == 'Office Supplies']
print(office_supplies.head(5))
print('As 7 primeiras Cidades com o maior valor de Venda na Categoria Office Supplies')
Cidades = office_supplies.groupby('Cidade')['Valor_Venda'].sum()
print(Cidades.sort_values(ascending=False).head(7))

print('Cidade com maior numeros de Vendas é:')
print(Cidades.idxmax())

