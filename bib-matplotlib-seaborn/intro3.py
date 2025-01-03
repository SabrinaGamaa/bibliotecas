import matplotlib.pyplot as plt
from pylab import *

x = linspace(0, 5, 10)
y = x ** 2

#sub plots
fig, axes = plt.subplots(1, 2, figsize = (10, 4))

#criar plot 1 
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title('Escala Padrao')

# cria plor 2
axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritima (y)')
plt.show()

