from keras import Sequential
from keras.layers import Dense
from keras.layers import Activation
import numpy as np
from data_prep import features, targets, features_test, targets_test

np.random.seed(21)

features = features.values
targets = targets.values
features_test = features_test.values
targets_test = targets_test.values

# epochs = 900
learnrate = 0.005

model = Sequential()

model.add(Dense(units=2,activation='softmax',input_dim=features.shape[1]))


model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])


#


# print(type(features))
model.fit(features, targets, epochs=3000, batch_size=features.shape[0])

# classes = model.predict()




