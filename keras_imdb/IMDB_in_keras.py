import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt
# %matplotlib inline

np.random.seed(42)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=1000)

# print(x_train.shape)
# print(x_test.shape)
#
# print(x_train)

tokenizer = Tokenizer(num_words=1000)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
print(x_train[0])

num_classes = 20
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_train.shape)
print(y_test.shape)

# building neural architechture:

model = Sequential()
model.add(Dense(units=1000, activation='relu', input_dim=1000))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=20, activation='softmax'))


model.compile(metrics=['accuracy'],loss='categorical_crossentropy',optimizer='adam')


model.fit(x_train, y_train, epochs=5)
score = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: ", score[1])

x_predict = input("Enter your movie review")

tokenizer_raw = Tokenizer(num_words=1000)
x_predict = tokenizer_raw.sequences_to_matrix(x_train, mode='binary')
model.predict(x_predict)
