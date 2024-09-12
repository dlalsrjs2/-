import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob

from matplotlib import pyplot as plt


data = pd.read_csv('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1.csv')
data.columns
len(data.columns)


plt.plot(data[['TOH [us]']]); plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/4_TOH [us]')
plt.plot(data[['Peak amplitude [mV]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/6_Peak amplitude [mV]')
plt.plot(data[['Duration [us]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/7_Duration [us]')
plt.plot(data[['Signal RMS [mVrms]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/8_Signal RMS [mVrms]')
plt.plot(data[['Noise RMS [mVrms]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/9_Noise RMS [mVrms]')
plt.plot(data[['ASL [mV]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/10_ASL [mV]')
plt.plot(data[['Rise-time [us]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/12_Rise-time [us]')
plt.plot(data[['Average frequency [kHz]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/13_Average frequency [kHz]')
plt.plot(data[['Signal strength [nVs]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/14_Signal strength [nVs]')
plt.plot(data[['Signal energy [EU]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/15_Signal energy [EU]')
plt.plot(data[['Noise energy [EU]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/16_Noise energy [EU]')
plt.plot(data[['Frequency centroid [kHz]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/17_Frequency centroid [kHz]')
plt.plot(data[['Peak frequency [kHz]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/18_Peak frequency [kHz]')
plt.plot(data[['Peak magnitude [mV]']]) ;plt.savefig('C:/Users/ADMIN/Desktop/Data2/Test/Channel 1_변수별 이미지/19_Peak magnitude [mV]')


#----------------------------------Signal RMS와 Noise RMS 비교----------------------------------

fig, ax = plt.subplots(2, 1, figsize=(12,8))
ax[0].plot(data[['Signal RMS [mVrms]']])
ax[1].plot(data[['Noise RMS [mVrms]']]) 
plt.show()




