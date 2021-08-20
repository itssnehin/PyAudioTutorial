import pyaudio
import numpy as np
import matplotlib.pyplot as plt


#constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'tmp/tmp.wav'

pa = pyaudio.PyAudio() # create a PyAudio instance
stream = pa.open(format=FORMAT,
				 channels=CHANNELS,
				 rate=RATE,
				 input=True,
				 frames_per_buffer=CHUNK)


#setup plot figure
fig, ax = plt.subplots(figsize=(14,6))
x = np.arange(0, 2 * CHUNK, 2)
ax.set_ylim(-200, 200)
ax.set_xlim(0, CHUNK) #make sure our x axis matched our chunk size
line, = ax.plot(x, np.random.rand(CHUNK))


while True:
	data = stream.read(CHUNK)
	numpydata = np.frombuffer(data, dtype = np.int16)
	line.set_ydata(numpydata)
	fig.canvas.draw()
	fig.canvas.flush_events()
	plt.pause(0.01)



