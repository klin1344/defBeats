import pyaudio
import numpy as np
import os, sys
#from acrcloud.recognizer import ACRCloudRecognizer
import wave
from threading import Thread
import requests
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

"""print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)"""
"""config = {
        #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
        'host':'us-west-2.api.acrcloud.com',
        'access_key':'6555f343e31d04d63f741c4bcf62b220', 
        'access_secret':'fRHnxtAd0gN7eyZ8tBBkIps1kvuDXXJPLFRKPmP0',
        'timeout':10 # seconds
}"""
#clientID = '403838581-8D151DF74D0555DBAB14867F30A53245' # Enter your Client ID here
#userID = pygn.register(clientID)
CHANNELS = 2
FORMAT = pyaudio.paInt16
# OUTPUT_FILENAME = "test.wav"

CHUNK = 2**12
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True,
              frames_per_buffer=CHUNK)


"""def write_file(frames):
        wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''

    print re.recognize_by_file('test.wav', 0)"""

    
def read_audio():
    #frames = []
    #write_thread = Thread(target = write_file, args = (frames,))

    while True:
        
        """rec_data = stream.read(CHUNK)
        frames.append(rec_data) # 2 bytes(16 bits) per channel

        if len(frames) > 100 and not write_thread.is_alive():
            write_thread = Thread(target = write_file, args = (frames,))
            write_thread.start()
            frames = []"""

        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        #print peak
        length = ((60.0 * peak) / (2 ** 11))
        #bars = "#" * int(length)

        if length < 4:
            pass
        if length >= 4:
            GPIO.output(3, GPIO.HIGH)
            # turn on 1
        else:
            GPIO.output(3, GPIO.LOW)

        if length >= 5:
            GPIO.output(4, GPIO.HIGH)
        else:
            GPIO.output(4, GPIO.LOW)
            # turn on 2

        if length >= 6:
            GPIO.output(9, GPIO.HIGH)
        else:
            GPIO.output(9, GPIO.LOW)
            #turn on 3
        if length >= 7:
            GPIO.output(14, GPIO.HIGH)
        else: 
            GPIO.output(14, GPIO.LOW)
            #turn on 4
        if length >= 8:
            GPIO.output(15, GPIO.HIGH)
        else:
            GPIO.output(15, GPIO.LOW)
            # turn on 5
        if length >= 9:
            GPIO.output(17, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.LOW)
            # turn on 5
        if length >= 9.5:
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
            # turn on 5
        if length >= 10:
            GPIO.output(22, GPIO.HIGH)
        else:
            GPIO.output(22, GPIO.LOW)
            # turn on 5
        if length >= 10.5:
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)

        if length >= 11:
            GPIO.output(25, GPIO.HIGH)
        else:
            GPIO.output(25, GPIO.LOW)
            # turn on 5
        #print "#", bars

read_audio()

stream.stop_stream()
stream.close()
p.terminate()
