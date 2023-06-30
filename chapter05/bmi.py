import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("../chapter04/bmi.csv")

csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

bclass = {"thin": [1, 0, 0], "normal": [0, 1, 0], "fat": [0, 0, 1]}
csv["label_pat"] = csv["label"].apply(lambda x: np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat = test_csv[["weight", "height"]]
test_ans = list(test_csv["label_pat"])

x = tf.Variable(tf.ones(shape=[None, 2], dtype=tf.float32))
y_ = tf.Variable(tf.ones(shape=[None, 3], dtype=tf.float32))

W = tf.Variable(tf.zeros([2, 3]))
b = tf.Variable(tf.zeros([3]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

optimizer = tf.keras.optimizers.SGD
