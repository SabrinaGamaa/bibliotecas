#5. Crie um array de 0 a 9 e eleve cada número ao quadrado.
import numpy as np
l1 = np.arange(0, 10)
print(f'O quadrado de cada numero do array: {np.square(l1)}')

print('-=' * 20)
#6. Crie uma matriz 3×3 com números de 1 a 9.
num = np.arange(1, 10).reshape(3, 3)
print(num)
print('-=' * 20)
# Usando a matriz criada no exercício anterior, extraia:
#O elemento da segunda linha e terceira coluna.
#A primeira coluna inteira.
print(f'Elemento da segunda linha e terceira coluna: {num[1, 2]}')
print(f'A primeira coluna inteira: {num[:,0]}')
print('-=' * 20)

#8. Transponha a matriz criada no exercício 6.
transponha = num.T
print('Matriz transponha: \n', transponha)

