import tensorflow as tf
# tensorflow is based on idea of creating computational graphs 
# tensors as nodes 
# and edged as computations 
hello_constant = tf.constant("Hello World")
    # in tensorflow we don't have basic data storage but tensors instead thus the name tensorflow 
    # for example in this code hello_constant is a 0 dimensional tensor (point tensor)
    # A = tf.constant(21)
    # here A is a int32 0 Dimensional tensor
    # B = tf.constant([21,21,21,221])
    # B is a 1 D int32 tensor
    # 
    # tf.constant is significant 
    # the property is that constant tensors dont change their values
    
x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.string)
    # giving values to tensors we define placeholders
    # we define the type of value the tensor will contain
    # and in the session we feed it with dicitonary 
    # if the value is not compatible with the input then it throws an error  


with tf.Session() as sess:
# A tensor flow session is an environment for running the graph
    output = sess.run(x,feed_dict={x: 121,y: 'this is spartA'})
    
# session.run fucniton evaluates the constant 
    print(output)

     