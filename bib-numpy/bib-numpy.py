import numpy as np 
l1 = np.array([10, 21, 32, 43, 54, 65, 75, 87])
print(l1)
print(type(l1))
print(l1.shape)

print(l1[4])
print(l1[1:4])
print(l1[1:4+1])
print('-' * 10)
indice = [1, 2, 5, 6]
print(l1[indice]) # retorne esses indices em cada numeração

print('-' * 10)
mask = (l1 % 2 == 0)
print(l1[mask]) # imprime valores pares
print(mask) # volta valores True para PAR e False para Falso

print('-' * 10)
l1[0] = 100
print(l1)
