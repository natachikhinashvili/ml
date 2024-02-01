import pandas as pd

iris_data = pd.read_csv("../iris.csv")

print("variety:", iris_data.variety)
print("shape:", iris_data.shape)
print("first 3 rows", iris_data.head(3))

print("keys:", iris_data.keys())
print("row nums:", len(iris_data))
print("data:", iris_data.head())


print("null values", iris_data.isnull().sum().sum())


print("info", iris_data.info())