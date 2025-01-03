import numpy as np
lista1 = np.arange(1, 10)
print(lista1)
print(f'A soma: {np.sum(lista1)}')
print('--' * 20)
print(f'Multiplicação de todos os elementos da lista: {np.prod(lista1)}')
print('--' * 20)
print(f'A soma acumulada: {np.cumsum(lista1)}')
print('--' * 20)
lista2 = np.array([3, 2, 1])
print(lista2)
lista3 = np.array([1, 2, 3])
print(lista3)
lista4 = np.add(lista2, lista3)
print(f' A soma das lista 2 e lista 3 formando agora alista 4: {lista4}')
print('--' * 20)

lista5 = np.array([[1, 2], [3, 4]])
lista6 = np.array([[5, 6], [0, 7]])
print(lista5.shape)
print(lista6.shape)
print('--' * 20)
print(lista5)
print('- -' * 15)
print(lista6)
#lista7 = np.dot(lista5, lista6)
# ou no lugar do dot eu posso usar @
lista7 = lista5 @ lista6
print('- -' * 15)
print(lista7)
print('--' * 20)
