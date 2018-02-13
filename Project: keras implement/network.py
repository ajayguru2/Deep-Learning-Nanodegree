from keras import Sequential
from keras.layers import Dense
from keras.layers import Activation
import numpy as np
from matplotlib import pyplot as plt

from data_prep import features, targets, features_test, targets_test

x = features.values
x_train = features_test.values
print(x.shape)
y = targets.values
print(y.shape)
plt.plot(x,y)
plt.show()



#Build model
model = Sequential()
model.add(Dense(units=36, activation='tanh', input_dim= 6))
model.add(Dense(units=24, activation='tanh'))
model.add(Dense(units=18, activation='tanh'))
model.add(Dense(units=12, activation='tanh'))
model.add(Dense(units=6, activation='tanh'))
model.add(Dense(units=1, activation='hard_sigmoid'))

#compile model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Train model
model.fit(x,y,epochs=10000)

# model.evaluate()


