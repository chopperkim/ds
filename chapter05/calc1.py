import tensorflow as tf

a = tf.constant(1234)
b = tf.constant(5000)


@tf.function
def add_op():
    return a + b


res = add_op()
print(res)
