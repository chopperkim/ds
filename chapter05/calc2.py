import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)


@tf.function
def calc1_op():
    return a + b * c


@tf.function
def calc2_op():
    return (a + b) * c


res1 = calc1_op()
res2 = calc2_op()

print(res1)
print(res2)
