from keras.datasets import mnist
from keras import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils


(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28 * 28).astype("float32") / 255
X_test = X_test.reshape(X_test.shape[0], 28 * 28).astype("float") / 255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


model = Sequential()
model.add(Dense(512, input_shape=(784, )))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))


model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

hist = model.fit(X_train, y_train, epochs=10)

score = model.evaluate(X_test, y_test, verbose=1)
print(f"loss={score[0]}")
print(f"accuracy={score[1]}")