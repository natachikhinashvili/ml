import pandas as pd

pd_data = pd.read_csv("../iris.csv")

print("data", pd_data.describe())

print(pd_data[pd_data['variety'].str.contains("Virginica")])


print("count", pd_data['variety'].value_counts())

print("dataid:", pd_data.head())

print("4data", pd_data.iloc[:, [1,2,3,4]].values)