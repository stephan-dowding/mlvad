import pyaudio
import io, sys

p = pyaudio.PyAudio()

try:
    filename=sys.argv[1]
except:
    print('ERROR: Usage - python playfile.py <filename> (e.g. python playfile.py voiceC')

data_file = io.FileIO('./sound/{}.pcm'.format(filename), mode='r')

FORMAT = p.get_format_from_width(width=2)
CHANNELS = 1
RATE = 16000
CHUNK = 16000

stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            frames_per_buffer=CHUNK)

print('playing...')

data = data_file.readall()
stream.write(data)

stream.close()
data_file.close()

print('done!')
