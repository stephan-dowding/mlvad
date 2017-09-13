
import pyaudio
import io

p = pyaudio.PyAudio()

data_file = io.FileIO('./sound/voiceC2.pcm', mode='x')

FORMAT = p.get_format_from_width(width=2)
CHANNELS = 1
RATE = 16000
CHUNK = 16000

stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK)

print('recording...')

for x in range(0, 10):
    data = stream.read(CHUNK)
    print()
    print(f"-{x}-")
    print(int.from_bytes(data[:2],byteorder='little', signed=True))
    print(int.from_bytes(data[-2:],byteorder='little', signed=True))

    data_file.write(data)
stream.stop_stream()
stream.close()
data_file.close()

print('done!')
