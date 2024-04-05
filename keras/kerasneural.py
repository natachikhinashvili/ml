from sklearn.model_selection import train_test_split
from pandas import read_csv

df = read_csv('../basic/iris.csv')

X = df.drop(columns=["variety"])
y = df["variety"]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
