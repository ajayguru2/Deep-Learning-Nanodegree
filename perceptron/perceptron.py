import numpy as np

class perceptron:
    def __init__(self):
        self.weights = np.empty(4)
        self.biased = 0

    def setWeights(self,w):
        self.weights = w
    def setBias(self,b):
        self.biased = b
    def runPerceptron(self,x):
        result = np.matmul(x,self.weights)
        result = result + self.biased
        if result >= 0:
            return 1
        else:
            return 0

if __name__ == '__main__':
    cell = perceptron()
    w = np.array([5, 6, -13])

    b = 3
    cell.setWeights(w)
    cell.setBias(b)
    x= np.array([2,3,4])
    x.shape = (1,3)

    print(cell.runPerceptron(x))










