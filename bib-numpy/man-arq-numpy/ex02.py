#3. Crie dois arrays, ambos com números de 1 a 5, e some-os.
import numpy as np
l1 = np.array([1, 2, 3, 4, 5])
l2 = np.array([1, 2, 3, 4, 5])
soma_lista = np.add(l1, l2)
print(f' A lista somadas: {soma_lista}')
print(f'A soma de todos os elemento é: {np.sum(soma_lista)}')

print('-=' * 20)
#4. Calcule a média e a variância de um array contendo os números [1, 2, 3, 4, 5]
media = np.mean(l1)
print(f'A media dos elementos 1, 2, 3, 4 e 5 é: {media}')
print(f'A variância é: {np.var(l1)}')

