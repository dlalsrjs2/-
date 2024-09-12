import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob

from matplotlib import pyplot as plt


data = pd.read_csv('C:/Users/ADMIN/Desktop/Data/Test2/wdat_AEC20240819065_00000000_CH03.csv')


n = len(data[['Time[us]']])
k = np.arange(n)
Fs = 1/0.005
T = n/Fs
freq = k/T

Y = np.fft.fft(data[['Voltage[mV]']])/n
Y = Y[range(int(n))]

fig, ax = plt.subplots(2, 1, figsize=(12,8))
ax[0].plot(data[['Time[us]']], data[['Voltage[mV]']])
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Voltage'); ax[0].grid(True)
ax[1].plot(freq, abs(Y), 'r', linestyle=' ', marker='^') 
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].vlines(freq, [0], abs(Y))
ax[1].set_xlim([0, 20]); ax[1].grid(True)
plt.show()


