
import tensorflow as tf

# TODO: Convert the following to TensorFlow:

x = tf.constant(10)
y = tf.constant(2)
inter = tf.divide(x,y)
result = tf.add(x,y)
# TODO: Print z from a session
with tf.Session() as sess:
    z = sess.run(result)
    print(z)
    