from perceptron import perceptron

class cluster():
    def __init__(self):
        self.inputNode = perceptron.perceptron()
        self.output1 = perceptron.perceptron()
        self.output2 = perceptron.perceptron()
        self.output3 = perceptron.perceptron()
        self.finalOutput = perceptron.perceptron()

    def runCluster(self,x):
        primaryOutput = self.inputNode.runPerceptron(x)
        secondaryInput = np.array([primaryOutput,0,0])



