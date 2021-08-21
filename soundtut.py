import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

pa = pyaudio.PyAudio() # create a PyAudio instance
stream = pa.open(format=FORMAT,
				 channels=CHANNELS,
				 rate=RATE,
				 input=True,
				 frames_per_buffer=CHUNK)




fig, ax = plt.subplots(2)
x = np.arange(10000)
y = np.random.randn(10000)

# Plot raw audio in time domain
line, = ax[0].plot(x,y)
ax[0].set_xlim(0, CHUNK)
ax[0].set_ylim(-500, 500)
ax[0].set_title("Audio Signal Time Domain")


#Plot FFT of the audio
line2, = ax[1].plot(x,y)
ax[1].set_xlim(0, 2000)
ax[1].set_ylim([0, 5000])
ax[1].set_title("FFT of Audio Signal")

# show the plot
plt.pause(0.01)
plt.tight_layout()



global stop
stop = False

#PSD attempt
while stop == False:
	try:
		data = stream.read(CHUNK)
		npdata = np.frombuffer(data, dtype=np.int16)

		f, P = signal.periodogram(npdata, RATE)
		index = signal.find_peaks(P, height=1e-2)[0][0]
		print(f[index])
		#display signals
		line.set_xdata(np.arange(len(npdata)))
		line.set_ydata(npdata)

		#display fft
		line2.set_xdata(f)
		line2.set_ydata(P)

		plt.pause(0.01)

	except KeyboardInterrupt:
		stop = True
	except:
		pass