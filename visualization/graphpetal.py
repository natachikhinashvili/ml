import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../basic/iris.csv')
x = df['petal.width']
y = df['petal.length']

plt.plot(x, color='orange', label='petal width')

plt.plot(y, color='blue', label='petal length')

plt.xlabel('Index')
plt.ylabel('Measurements')
plt.legend()

plt.show()