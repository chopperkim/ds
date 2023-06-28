from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import time

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w, h], axis=1)

X_train, X_test, y_train, y_test = train_test_split(wh, label)

clf = svm.SVC()

start = time.time()

clf.fit(X_train, y_train)

predict = clf.predict(X_test)

end = time.time()

ac_score = metrics.accuracy_score(y_test, predict)
cl_report = metrics.classification_report(y_test, predict)

print(f"정답률 = {ac_score}")
print(f"리포트 = {cl_report}")
print(f"실행시간 = {end - start}")


