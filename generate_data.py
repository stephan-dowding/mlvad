import io, random
import numpy as np

DATA_AUGMENTATION_MULTIPLIER = 6
chunk_size = 480
samples = []
answer = []
validation_samples = []
validation_answer = []
speech_audiofiles = ['voiceC', 'voiceC2', 'voiceD2', 'voiceE',\
                     'voiceJ2', 'voiceO', 'voiceO2', 'voiceR', \
                     'voiceS2', 'voiceW']

non_speech_audiofiles = ['airblower', 'quiet', 'quiet2', 'not_voice', \
                        'allhands', 'allhands2']

def generate_sample_data(audiofile, label):
    data_file = io.FileIO('./sound/{}.pcm'.format(audiofile), mode='r')

    data = data_file.readall()
    data_file.close()

    sample_length = len(data)
    start = random.randint(chunk_size,sample_length//8)
    end = random.randint(sample_length // 8 * 7, sample_length)

    for x in range(start, end, chunk_size):
        chunk = data[x:(x+chunk_size)]
        sample = []
        for s in range(0, chunk_size, 2):
            p = int.from_bytes(chunk[s:(s+2)],byteorder='little', signed=True)
            sample.append(p)

        samples.append(sample)
        answer.append(label)

for audiofile in speech_audiofiles:
    for i in range(DATA_AUGMENTATION_MULTIPLIER):
        generate_sample_data(audiofile, label=1)

for audiofile in non_speech_audiofiles:
    for i in range(DATA_AUGMENTATION_MULTIPLIER):
        generate_sample_data(audiofile, label=0)

X = np.mat(samples)
y = np.array(answer)

np.save('./data/samples.npy', X)
np.save('./data/labels.npy', y)
