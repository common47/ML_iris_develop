import pandas as pd


# your project absolute path
path = "/Users/commo/Documents/IDS/ML_iris_develop"

model = pd.read_pickle(path + "/new_model.pkl")

print(model)

print(model.__dict__)


# print(model[1])

print(str(model))

print(model._y)

print(model._x)
