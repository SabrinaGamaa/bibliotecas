import numpy as np
import os
import matplotlib.pyplot as plt
filename = os.path.join('C:/Users/Sabrina Gama/Downloads/python/bibliotecas/bib-numpy/man-arq-numpy/Notebooks/dataset.csv')

lista1 = np.loadtxt(filename, delimiter= ',', usecols=(0, 1, 2, 3), skiprows=1)
print('Tem linha e colunas',lista1.shape)

var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0, 1), skiprows=1, unpack= True)
plt.plot(var1, var2, 'o', markersize=6, color='red')
plt.show()
