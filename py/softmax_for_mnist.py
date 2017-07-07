
# coding: utf-8

# In[ ]:

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# data
mnist = input_data.read_data_sets("MNIST_data", one_hot = True)


# In[7]:

batch_size = 100
n_batch = mnist.train.num_examples // batch_size
print(n_batch)


# In[8]:

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax(tf.matmul(x, W) + b)


# In[9]:

loss = tf.reduce_mean(tf.square(y - prediction))


# In[10]:

train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)


# In[12]:

init = tf.global_variables_initializer()


# In[15]:

correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# In[18]:

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(20):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict = {x:batch_xs, y:batch_ys})
        acc= sess.run(accuracy, feed_dict = {x:mnist.test.images, y:mnist.test.labels})
        print("epoch: " + str(epoch) + " test accuracy" + str(acc))


# In[ ]:



