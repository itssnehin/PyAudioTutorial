import pyaudio
import numpy
import matplotlib
import wave
import thread
import time
import subprocess


#constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'tmp/tmp.wav'

pa = pyaudio.PyAudio() # create a PyAudio instance
