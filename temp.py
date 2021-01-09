import pandas as pd

import tensorflow.compat.v1 as tf
 
#a = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12], shape=[2, 3, 2])
#b = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3, 1])
 
#c = a * b
#d = tf.multiply(a, b)

sess = tf.Session()
#a,b,c,d=sess.run([a,b,c,d])

#print(a)
#print(b)
#print(c)
#print(d)

a = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12], shape=[1,12])
b= tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12], shape=[3,4])

print(sess.run(tf.add(a,a)))


