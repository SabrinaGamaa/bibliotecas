import numpy as np
import pandas as pd
from pandas import DataFrame
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

df2 = DataFrame(dados,
                columns= ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index= ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

# USANDO NUMPY E PANDAS PARA MANIPULAÇÃO DE DADOS
print(df2.head())
print('- -' * 15)
print(df2.dtypes)
print('-=' * 20)

#RESUMO ESTATÍSTICO DO DATAFRAME
print(df2.describe())
print('-=' * 20)
# verificar se tem valor NaN 
print(df2.isna())
print('- -' * 15)
print(df2['Taxa Crescimento'].isna())
df2['Taxa Crescimento'] = np.arange(5.)
print(df2)
print('-=' * 20)
print(df2.describe())
print('-=' * 20)
print(df2[2:4])
print('- -' * 15)
print(df2[['Taxa Desemprego', 'Ano']])
print('- -' * 15)
print(df2[df2['Taxa Desemprego'] > 2])
