import numpy as np

def sigmoid(x):
    return (1/1+np.exp(-x))
def sigmoidPrime(x):
    return sigmoid(x)*(1 - sigmoid(x))




class perceptron:
    def __init__(self):
        self.weights = np.empty(4)
        self.biased = 0

    def setWeights(self,w):
        self.weights = w
    def setBias(self,b):
        self.biased = b
    def runPerceptron(self,x,w):
        h = np.dot(x,w)
        result = nn_output = sigmoid(h)
        print(result)




if __name__ == '__main__':
    cell = perceptron()
    w = np.array([5, 6, -13])

    b = 3
    cell.setWeights(w)
    cell.setBias(b)
    x= np.array([2,3,4])


    print(cell.runPerceptron(x,w))










