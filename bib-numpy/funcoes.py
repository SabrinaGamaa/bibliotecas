import numpy as ar
lista = ar.array([1, 2, 3, 4, 5])
print(lista)
print(lista.cumsum()) # soma os numeros em sequencia
print(lista.cumprod()) # multiplica os numeros em sequencia

lista2 = ar.arange(0, 50, 5)
print(lista2)
print(ar.shape(lista2))

lista3 = ar.zeros(20)
print(lista3)
print('==' * 20)

lista4 = ar.eye(5)
print(lista4)
print('==' * 20)

lista5 = ar.diag(ar.array([1, 2, 3, 4]))
print(lista5)
print('==' * 20)

lista6 = ar.array([True, False, False, True])
print(lista6)
print('==' * 20)

lista7 = ar.array(['Linguagem python', 'PHP', 'JAVA'])
print(lista7)
print('==' * 20)

lista8 = ar.linspace(0, 10)
print('==' * 20)

lista9 = ar.linspace(0, 10, 15)
print(lista9)
print('==' * 20)

lista10 = ar.logspace(0, 5, 10)
print(lista10)
print('==' * 20)

lista11 = ar.array([[1, 2, 3], [4, 5, 6]])
print(lista11)
print('==' * 20)

lista12 = ar.ones((2, 3))
print(lista12)
print('==' * 20)

criar_lista = [[13, 25, 46], [54, 32, 64], [87, 90, 43]]
lista13 = ar.matrix(criar_lista)
print(lista13)
print('Tamanho da coluna')
colu = ar.shape(lista13)
print(colu)
print('Tamanho da matrix')
mat = ar.size(lista13)
print(mat)
print('==' * 20)
