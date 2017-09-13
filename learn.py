import keras
import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import io

chunk_size = 480

model = Sequential()
model.add(Dense(128, activation='tanh', input_dim=(chunk_size//2)))
# model.add(Dropout(0.25))

for x in range(3):
    model.add(Dense(128, activation='tanh'))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


samples = []
answer = []
validation_samples = []
validation_answer = []

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


data_file = io.FileIO('./sound/voiceW.pcm', mode='r')
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
    answer.append(1)


data_file = io.FileIO('./sound/allhands.pcm', mode='r')
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
    answer.append(1)

data_file = io.FileIO('./sound/not_voice.pcm', mode='r')
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

data_file = io.FileIO('./sound/voiceS.pcm', mode='r')
data = data_file.readall()
data_file.close()

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    validation_samples.append(sample)
    validation_answer.append(1)

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

    validation_samples.append(sample)
    validation_answer.append(0)

data_file = io.FileIO('./sound/allhands2.pcm', mode='r')
data = data_file.readall()
data_file.close()

# skip first chunk
for x in range(chunk_size, end, chunk_size):
    chunk = data[x:(x+chunk_size)]
    sample = []
    for s in range(0, chunk_size, 2):
        p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
        sample.append(p)

    validation_samples.append(sample)
    validation_answer.append(0)


X = numpy.mat(samples)
y = numpy.array(answer)

val_X = numpy.mat(validation_samples)
val_y = numpy.array(validation_answer)

model.fit(X, y, epochs=50, batch_size=32, validation_data=(val_X, val_y))

model.save("vad.h5")
#print(model.to_yaml())
