import numpy as np
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

np.random.seed(42)
n = 1000
fumantes_smokers = 0.2

flag_fumantes = np.random.rand(n) < fumantes_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumantes': flag_fumantes})
print(dados.head(5))
print('-=' * 40)

# Cria os dados para a variavel flag_fumantes
dados['flag_fumantes'] = dados['flag_fumantes'].map({True: 'Fumante', False: 'Não fumante'})
print(dados.head(7))

sea.set_theme(style='ticks')

sea.lmplot(x = 'altura',
           y = 'peso',
           data=dados,
           hue = 'flag_fumantes',
           palette= ['tab:blue', 'tab:orange'],
           height=7)

plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso de Fumante e não Fumante')

plt.show()

