import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("../basic/iris.csv")
x = df['sepal.length']
y = df['sepal.width']

plt.plot(x, color='green', label='Sepal Length')

plt.plot(y, color='red', label='Sepal Width')

plt.xlabel('Index')
plt.ylabel('Measurements')
plt.legend()

plt.show()