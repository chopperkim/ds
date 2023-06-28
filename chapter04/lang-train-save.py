from sklearn import svm
import joblib
import json

with open("dataset/lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]


clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

joblib.dump(clf, "dataset/lang/freq.pkl")
print("ok")

