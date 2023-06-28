import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

mr = pd.read_csv("dataset/mushroom.csv", header=None)

label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row[0])
    row_data = []
    for v in row[1:]:
        row_data.append(ord(v))
    data.append(row_data)
    
data_train, data_test, label_train, label_test = train_test_split(data, label)

clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)

print(f"정답률 = {ac_score}")
print(f"리포트 = {cl_report}")


