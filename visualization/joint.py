from seaborn import jointplot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../basic/iris.csv')

slen = df['sepal.length']
swid = df['sepal.width']
concatenated = pd.concat([slen, swid], axis=1)
jointplot(concatenated)

plt.ylabel('Index')
plt.xlabel('Measurements')

plt.show()