#!/usr/bin/env python


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

# data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
batch_size = 100
num_batch = mnist.train.num_examples // batch_size
Nepoches = 30

# placeholder
x = tf.placeholder(dtype = tf.float64, shape = [None, 784])
y = tf.placeholder(dtype = tf.float64, shape = [None, 10])

# varviables
w = tf.Variable(np.random.rand(784, 10))
b = tf.Variable(np.random.rand(1, 10))

# graph
predict = tf.nn.softmax(tf.add(tf.matmul(x, w), b))
loss = tf.reduce_mean(tf.square(predict - y))

# optimize
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

# accuracy
res_flag = tf.equal(tf.argmax(y, 1), tf.argmax(predict, 1))
accuracy = tf.reduce_mean(tf.cast(res_flag, tf.float32))

# session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(Nepoches):
        for _ in range(num_batch):
            x_feed, y_feed = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict = {x:x_feed, y:y_feed})
        # after finish one epoch. cal the accury
        print("epoch:%d" % i)
        print("\t", sess.run(accuracy, feed_dict = {x: mnist.test.images, y:mnist.test.labels}))
        print("\tb: ", b.eval())
    # get all the predict value of softmax.
    b = sess.run(predict, feed_dict = {x: mnist.test.images})
    print(b.shape)
    row, col = b.shape
    for i in range(row):
        print(b[i,:])

