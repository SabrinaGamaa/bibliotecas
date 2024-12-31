#1. Crie um array NumPy com os números inteiros de 1 a 10.
import numpy as np
lista = np.array(np.arange(1, 11))
print(lista)

print('=-' * 20)
#2. Multiplique cada elemento do array criado no exercício anterior por 2 e exiba o resultado.
multi = np.multiply(lista, 2)
print(multi)

print('=-' * 20)
