import pandas as pd

# pandas
dados = {'Nome': ['Maria', 'Joao'], 'Idade': [22, 35]}
df = pd.DataFrame(dados)
print(df)

# selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.python.org')
print(driver.title)
driver.quit()

# matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafico de exemplo')
plt.show()

