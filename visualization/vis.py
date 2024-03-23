import matplotlib.pyplot as plt
import pandas as pd

iris_df = pd.read_csv("../basic/iris.csv")
varieties = pd.Categorical(iris_df['variety'])
countofitems = varieties.value_counts()

plt.figure()
plt.title('Bar Plot of Iris Dataset')

countofitems.plot(kind='bar')

plt.xlabel('Values')
plt.ylabel('Count')
plt.show()