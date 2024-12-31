import numpy as np
import os
filename = os.path.join('')

lista1 = np.loadtxt(filename, delimiter= ',', usecols=(0, 1, 2, 3), skiprows=1)
print(lista1)
