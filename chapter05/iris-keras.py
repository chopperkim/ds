import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split


df = pd.read_csv("../data/iris3.csv")
sns.pairplot(df, hue='species')
plt.savefig("iris-pairplot")

X = df.iloc[:, 0:4]
y = df.iloc[:, 4]

y = pd.get_dummies(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=50, batch_size=10)

score = model.evaluate(X_test, y_test)
print(f"loss={score[0]}")
print(f"accuracy={score[1]}")

