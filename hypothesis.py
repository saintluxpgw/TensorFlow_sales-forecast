import tensorflow as tf

dataX = [5, 6, 7, 8, 9, 10, 11, 12]
dataY = [138748310, 293083260, 599818677, 806742572, 988609172, 1220109100]
weight = tf.Variable(tf.random.uniform([1], -100, 100))
bias = tf.Variable(tf.random.uniform([1], -100, 100))
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)
hypothesis = weight * X + bias
cost = tf.reduce_mean(tf.square(hypothesis - Y))
jump = tf.Variable(0.01)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(jump)
train = optimizer.minimize(cost)
init = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()
session.run(init)

for i in range(5001):sada
    session.run(train, feed_dict={X: dataX, Y: dataY})
    if i % 500 == 0:
        print (i, session.run(cost, feed_dict={X: dataX, Y: dataY}), session.run(weight), session.run(bias))

print(session.run(hypothesis, feed_dict={X: [10]}))


# mnist = tf.keras.datasets.mnist
