import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os
import traceback

def clear():
    # check if windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:  # or unix
        _ = os.system('clear')

# constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
INPUT_INDEX = 1

pa = pyaudio.PyAudio()  # create a PyAudio instance
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 input_device_index=INPUT_INDEX,
                 frames_per_buffer=CHUNK
                 )




fig, ax = plt.subplots(2)
x = np.arange(10000)
y = np.random.randn(10000)

# Plot raw audio in time domain
line, = ax[0].plot(x,y)
ax[0].set_xlim(0, CHUNK)
ax[0].set_ylim(-500, 500)
ax[0].set_title("Audio Signal Time Domain")


# Plot FFT of the audio
line2, = ax[1].plot(x,y)
ax[1].set_xlim(0, 2000)
ax[1].set_ylim([0, 200])
ax[1].set_title("FFT of Audio Signal")

# show the plot
plt.pause(0.01)
plt.tight_layout()

global stop
stop = False

# PSD attempt
while stop is False:
    try:
        data = stream.read(CHUNK*2)
        npdata = np.frombuffer(data, dtype=np.int16)
        #print(npdata)
        f, P = signal.periodogram(npdata, RATE)
        #index,_ = signal.find_peaks(P, height=1e-2)[0][0]
        #clear()
        #print(f[index])
        # display signals
        line.set_xdata(np.arange(len(npdata)))
        line.set_ydata(npdata)

        # display fft
        PdB = 10 * np.where(P>0, np.log10(P), 0)
        line2.set_xdata(f)
        line2.set_ydata(PdB)

        plt.pause(0.01)

    except KeyboardInterrupt:
        stop = True
    except Exception as e:
        traceback.print_exc()