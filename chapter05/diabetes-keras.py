import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv("../data/pima-indians-diabetes3.csv")

color_map = plt.cm.gist_heat
plt.figure(figsize=(12, 12))

sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=color_map, linecolor="white", annot=True)
plt.show()

plt.hist(x=[df.plasma[df.diabetes==0], df.plasma[df.diabetes==1]], bins=30, histtype='barstacked', label=['normal', 'diabetes'])
plt.legend()
plt.show()

plt.hist(x=[df.bmi[df.diabetes==0], df.bmi[df.diabetes==1]], bins=30, histtype="barstacked", label=['normal', 'diabetes'])
plt.legend()
plt.show()

X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu', name="Dense_1"))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X, y, epochs=200, batch_size=10)
score = model.evaluate(X, y, verbose=1)

print(f"loss: {score[0]}")
print(f"accuracy: {score[1]}")