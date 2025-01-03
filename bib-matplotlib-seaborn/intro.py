import matplotlib.pyplot as plt
plt.plot([1, 3, 5,], [2, 4, 7])
plt.show()


# Agora vou passar metodos
x = [2, 3, 5]
y = [3, 5, 7]
plt.plot(x, y)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 2')
plt.title('TESTE DE PLOT')
plt.show()

plt.plot(x, y, label = 'Grafico com Matplotlib', color = 'green')
plt.legend()
plt.show()

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

#barras
plt.bar(x, y, label = 'Lista 1', color = 'blue')
plt.bar(x2, y2, label = 'Lista 2', color = 'red')
plt.legend()
plt.show()

# criar um indice para fazer o grafico
idades = [22, 21, 44, 32, 23, 45, 64, 32, 23, 4, 64, 65, 34, 23, 12, 15, 17]
ids = [x for x in range(len(idades))]
print(ids)

plt.bar(ids, idades, label = 'Idades', color = 'pink')
plt.title('Idades das Pessoas')
plt.legend()
plt.show()

# Use o arquivo aulas
