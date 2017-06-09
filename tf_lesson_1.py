import tensorflow as tf
import os

# env
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# define the graph

hello_op = tf.constant('hello, tf')
a = tf.constant(1)
b = tf.constant(11)

add_op = tf.add(a, b)

# define the session to run the graph

with tf.Session() as sess:
    print(sess.run(hello_op))
    print(sess.run(add_op))

