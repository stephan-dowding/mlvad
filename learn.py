import io, random
import keras
import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from sklearn.model_selection import train_test_split

chunk_size = 480

model = Sequential()
model.add(Dense(128, activation='tanh', input_dim=(chunk_size//2)))
model.add(Dropout(0.25))
for x in range(3):
    model.add(Dense(128, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

X = numpy.load('./data/samples.npy')
y = numpy.load('./data/labels.npy')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

model.save("vad.h5")
#print(model.to_yaml())
