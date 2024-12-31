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
print('--' * 20)

print('NumPy decide os dados')
x = np.array([1, 2])
print(x)
print('NumPy decide o tipo do dado')
y = np.array([1.0, 2.0])
print(y)
print('Forçamos um tipo de dado')
z = np.array([1, 2], dtype=np.float64)
print(z)
print('--' * 20)
print(x.dtype, y.dtype, z.dtype)
print('--' * 20)

lista2 = np.array([[23, 54, 32, 64], [43, 64, 21, 65]], dtype=float)
print(lista2)
print(lista2.dtype)
print('--' * 20)


# itemsize ele retorna o tamanho em bytes de cada elemento array
print(lista2.itemsize)
print(lista2.nbytes)
# numeros de dimensoes
print(lista2.ndim)
