import pandas as pd
from sklearn import svm, metrics, ensemble
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/pima-indians-diabetes3.csv')

X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

X_train, X_test, y_train, y_test = train_test_split(X, y)

# clf = svm.SVC()
clf = ensemble.RandomForestClassifier
clf.fit(X_train, y_train)

predict = clf.predict(X_test)

ac_score = metrics.accuracy_score(y_test, predict)
cl_report = metrics.classification_report(y_test, predict)

print(f"정답률={ac_score}")
print(f"리포트={cl_report}")
