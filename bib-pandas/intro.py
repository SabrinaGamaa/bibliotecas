from pandas import DataFrame
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

# DataFrame transfoma o dicionarios em tabelas
df = DataFrame(dados)
print(df)
print(type(df))
print('-=' * 20)
# Reorganizando as colunas
reo = DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Ano'])
print(reo)
print('-=' * 20)

# Adicionando uma coluna e colocando index para cada enumerate
df2 = DataFrame(dados,
                columns= ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index= ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2)
print('-=' * 20)
print(df2.values)
print('-=' * 20)
print(df2.dtypes)
print('-=' * 20)
print(df2.columns)
print('-=' * 20)
print(df2['Estado'])
print('-=' * 20)
print(df2[['Estado', 'Ano']])
print('-=' * 20)
print(df2.index)
print(df2.filter(items=['estado3'], axis = 0))
print('-=' * 20)
