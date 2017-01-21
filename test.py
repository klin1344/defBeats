import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak = np.average(np.abs(data)) * 2
    bars = int(60 * peak / 2 ** 16)
    print "#", "#" * bars

stream.stop_stream()
stream.close()
p.terminate()