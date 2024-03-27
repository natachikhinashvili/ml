import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('../basic/iris.csv')
sepleng = df['sepal.length']
sepwidth = df['sepal.width']
petleng = df['petal.length']
petwidth = df['petal.width']

index = range(len(df))

plt.plot(index, sepleng, color='green', label='Sepal Length')
plt.plot(index, sepwidth, color='red', label='Sepal Width')
plt.plot(index, petleng, color='blue', label='Petal Length')
plt.plot(index, petwidth, color='orange', label='Petal Width')

plt.xlabel('Index')
plt.ylabel('Measurements')
plt.legend()

plt.show()