import tensorflow as tf 
# since constants are rigid vectors and in our linear function 
# y = Wx + b we have to modify weights
# So we come to the idea of tf.variables

x = tf.Variable(5)

# we use tf.global_variables_initializer() to initialise the states of our variables
# using the tf.variable creates a varible tensor but it needs to be initialised
init = tf.global_variables_initializer()

with tf.Session() as sess:
    output = sess.run(init)
    print(output)
