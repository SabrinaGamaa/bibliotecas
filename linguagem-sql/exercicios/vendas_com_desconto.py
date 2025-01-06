## Pergunta de Negócio 7 (Desafio Nível Júnior):
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
### Quantas Vendas Receberiam 15% de Desconto?

import pandas as pd
import numpy as np
dados = pd.read_csv('linguagem-sql/exercicios/dados/dataset.csv')
print(dados.columns)
dados['Desconto'] = np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)
print(dados['Desconto'].value_counts())
print('-=' * 60)

## Pergunta de Negócio 8 (Desafio Nível Master):
### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
dados['Valor_Venda_Desconto'] = dados['Valor_Venda'] - (dados['Desconto'] * dados['Valor_Venda'])

valor_vendas_antes_desconto = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda']
valor_vendas_depois_desconto = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda_Desconto']
print(f'Media de venda ANTES do desconto de 15%: \n {valor_vendas_antes_desconto.mean():.2f}')
print(f'Media de venda DEPOIS do desconto de 15%: \n {valor_vendas_depois_desconto.mean():.2f}')
