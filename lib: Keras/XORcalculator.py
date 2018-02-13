import numpy as np
from keras import Sequential
from keras.layers import Dense
from keras.layers import Activation

x = np.array([(0,0),(0,1),(1,0),(1,1)])

y = np.array([0,1,1,0])

model = Sequential()
model.add(Dense(1000, activation='tanh', input_dim=2))
model.add(Dense(800,activation='relu'))
model.add(Dense(1,activation='softmax'))

model.compile(optimizer='sgd',metrics=['accuracy'],loss="mean_squared_error")
model.fit(x,y,epochs=50)

loss_and_metrics = model.evaluate(x, y, batch_size=128)

x_predict = np.array([(1,1)])
print(model.predict(x_predict))

