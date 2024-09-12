import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob

from matplotlib import pyplot as plt


Origin_data = pd.read_csv('C:/Users/ADMIN/Desktop/Data/Test2/wdat_AEC20240819065_00000000_CH03.csv')
FFT_data = pd.read_csv('C:/Users/ADMIN/Desktop/Data/Test2/fdat_AEC20240819065_00000000_CH03.csv')

Origin_data.columns
FFT_data.columns

fig, ax = plt.subplots(2, 1, figsize=(12,8))
ax[0].plot(Origin_data[['Time[us]']], Origin_data[['Voltage[mV]']])
ax[1].plot(FFT_data[['Amplitude[dBuV]']], abs(FFT_data[['Frequency[kHz]']])) 
plt.show()

