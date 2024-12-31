import numpy as np
print('Criar uma matrix')
criar_lista = [[13, 25, 46], [54, 32, 64], [87, 90, 43]]
lista1 = np.matrix(criar_lista)
print(lista1)
print('--' * 20)

# indexação da matrix
print(lista1[2, 1])
print(lista1[0:2,1])
print('--' * 20)

print('Alterar um elemento da matrix')
lista1[1, 0] = 100
print(lista1)
