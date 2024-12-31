import numpy as np
# criar uma matrix com valor na diag
lista1 = np.diag(np.arange(3))
print(lista1)
print('--' * 20)
print(lista1[1, 1])
print('--' * 20)
print(lista1[1])
print('--' * 20)
print('Coluna: ')
print(lista1[:,2])
print('--' * 20)
lista2 = np.arange(10)
print(lista2)
lista2[2:9:3]
print('--' * 20)
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print('Faz uma comparação')
print(a == b)

print('--' * 20)
print(lista2.max())
print(lista2.min())

lista4 = np.array([1.3, 2.5, 2.6])
print(np.around(lista4))
