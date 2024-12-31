import numpy as np
lista1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(lista1)
print('--' * 20)

print('Fazer com que a matriz se transforme em uma lista simples')
print(lista1.flatten())
print('--' * 20)

lista2 = np.array([1, 2, 3])
print('Repetir cada elemento')
print(lista2.repeat(3))
print('--' * 20)
print('Cria uma copia e repete a copia na mesma lista')
print(np.tile(lista2, 3))
print('--' * 20)
print('Criando uma copia extada')
lista3 = np.array([5, 6])
lista4 = np.copy(lista3)
print(lista4)
