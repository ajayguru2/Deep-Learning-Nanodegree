import numpy as np
# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
   Y = np.float_(Y)
   P = np.float_(P)
   return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


class tester():
    Y = [1,0,0,1,1,1]
    P = [0.32,0.98,0.22,0.45,0.77,0.556]
    print(cross_entropy(Y,P))

if __name__ == '__main__':
    tester()