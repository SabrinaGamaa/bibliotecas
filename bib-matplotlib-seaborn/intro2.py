import matplotlib.pylab as plt
from pylab import *

x = linspace(0, 3, 5)
y = x ** 2

fig = plt.figure()
# definir as escalas dos eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# Corrigindo para usar o eixo específico
axes1.plot(x, y, color='red')

axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Grafico de Linha')

axes2.plot(x, y, label = 'green')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('Segundo Grafico')
plt.show()

