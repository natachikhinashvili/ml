import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../basic/iris.csv')
varieties = pd.Categorical(df['variety'])
count = varieties.value_counts()

plt.figure()
plt.title('Pie chart of frequency of values')

count.plot(kind='pie')

plt.show()