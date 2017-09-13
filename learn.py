import keras
import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

model = Sequential()
model.add(Dense(128, activation='relu', input_dim=320))
model.add(Dropout(0.25))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


import io

chunk_size = 640

samples = []
answer = []

data_file = io.FileIO('./sound/voiceC.pcm', mode='r')
data = data_file.readall()
data_file.close()

end = len(data)

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    samples.append(sample)
    answer.append(1)


data_file = io.FileIO('./sound/quiet.pcm', mode='r')
data = data_file.readall()
data_file.close()

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    samples.append(sample)
    answer.append(0)


#data_file = io.FileIO('./sound/allhands.pcm', mode='r')
data_file = io.FileIO('./sound/quiet2.pcm', mode='r')
data = data_file.readall()
data_file.close()

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    samples.append(sample)
    answer.append(0)

data_file = io.FileIO('./sound/voiceR.pcm', mode='r')
data = data_file.readall()
data_file.close()

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    samples.append(sample)
    answer.append(0)


X = numpy.mat(samples)
y = numpy.array(answer)

model.fit(X, y, epochs=100, batch_size=32)
