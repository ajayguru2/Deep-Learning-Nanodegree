import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derSigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


learningRate = 0.1
x = np.array([1, 2, 3, 4])
y = np.array(0.5)
w = np.array([0.5, -0.5, 0.3, 0.1])

# output of the first perceptron:
yPrime = sigmoid(np.dot(x, w))
error = y - yPrime
errorTerm = error*derSigmoid(np.dot(x,w))

changeinWeights = learningRate*errorTerm*x
w = w + changeinWeights

print('Neural Network output:')
print(sigmoid(np.dot(x,w)))
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(changeinWeights)
print('New weights:')
print(w)

