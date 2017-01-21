from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
import numpy
import time
from scipy.io.wavfile import read,write
import RPi.GPIO as GPIO

numpy.set_printoptions(threshold='nan') # this is just to be able to print out all elements of the numpy array



Fs = 44100;  # sampling rate

rate,data=read('test.wav')
y=data[:,1] # y is the amplitude
lungime=len(y)
timp=len(y)/44100.
t=linspace(0,timp,len(y)) # t is time of the wav audio file

# WIP - how do we read through the entire array of amplitude values in real time?
# this just divides total time by number of data points in y
interval = t[-1] / float(len(y))

# set up GPIO on RPI
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

for item in y:
	time.sleep(interval) # this probably isn't the best idea - need to find out how to traverse list in real time in accordance with audio
	if math.abs(item) > 500: # only turn on the GPIO pin on very high amplitudes - needs tweaking
		GPIO.output(18, GPIO.HIGH)
		time.sleep(interval) # how long we should turn the motor on for - again, needs much better logic
							# maybe we could iterate through every 4th data point in y? not sure yet
		GPIO.output(18, GPIO.LOW) # turn off pin

