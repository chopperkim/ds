import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

csv = pd.read_csv("dataset/iris.csv")

data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print(f"각각의 정답률 = {scores}")
print(f"평균 정답률 = {scores.mean()}")