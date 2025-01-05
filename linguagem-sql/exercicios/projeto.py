import pandas as pd
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
print('-=' * 60)

## Pergunta de Negócio 1:
### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
cidade_maior_valor_venda = 