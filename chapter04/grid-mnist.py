import pandas as pd
from sklearn import model_selection, svm, metrics, datasets
from sklearn.model_selection import GridSearchCV, train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(data, digits.target)

params = [
    {"C": [1, 10, 100, 1000], "kernel": ["linear"]},
    {"C": [1, 10, 100, 1000], "kernel": ["rbf"], "gamma": [0.001, 0.0001]}
]

clf = GridSearchCV(svm.SVC(), params, n_jobs=-1)
clf.fit(X_train, y_train)
print(f"학습기 = {clf.best_estimator_}")

pre = clf.predict(X_test)
ac_score = metrics.accuracy_score(y_test, pre)
print(f"정답률 = {ac_score}")
