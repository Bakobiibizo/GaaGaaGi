import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def plot_spectrogram(file_path):
    # Read the audio file
    rate, data = wavfile.read(file_path)

    # Calculate the spectrogram
    f, t, Sxx = signal.spectrogram(data, rate)

    # Plot the spectrogram
    plt.pcolormesh(t, f, np.log(Sxx))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

plot_spectrogram('./out/combined.wav')