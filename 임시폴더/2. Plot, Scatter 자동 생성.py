import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from matplotlib import pyplot as plt


file_path = os.listdir("C:/Users/ADMIN/Desktop/Data/원본 데이터 Total/")

#----------------------------------- Plot, Scatter 한번에 자동으로 그리기 -----------------------------------
for i in file_path:
    globals()[i] = pd.read_csv(f'C:/Users/ADMIN/Desktop/Data/원본 데이터 Total/{i}')    
    for i in file_path:
        fig, ax = plt.subplots(2,1, figsize = (32,18))
        ax[0].plot(globals()[i][['Time[us]']], globals()[i][['Voltage[mV]']])
        ax[0].set_title("Plot")
#        ax[0].xlabel('Time[us]', fontsize= 25)                             # x축 라벨 설정
#        ax[0].xticks(fontsize = 25) 
#        ax[0].ylabel('Voltage[mV]', fontsize= 25)                            # y축 라벨 설정
#        ax[0].yticks(fontsize = 25) 
        
        ax[1].scatter(globals()[i][['Time[us]']], globals()[i][['Voltage[mV]']])
        ax[1].set_title("Scatter")
#        ax[1].xlabel('Time[us]', fontsize= 25)                             # x축 라벨 설정
#        ax[1].xticks(fontsize = 25) 
#        ax[1].ylabel('Voltage[mV]', fontsize= 25)                            # y축 라벨 설정
#        ax[1].yticks(fontsize = 25)
        plt.suptitle(i)
        plt.tight_layout()
        plt.show()
        break
    
#--------------------------------------------------------------------------------------------------------



#----------------------------------- Plot, Scatter 각각 자동으로 그리기 -----------------------------------
#----------------------------------- Plot, Scatter을 한번에 만들면 메모리 오류가 뜸 -----------------------------------
for i in file_path:
    globals()[i] = pd.read_csv(f'C:/Users/ADMIN/Desktop/Data/원본 데이터 Total/{i}')    
    plt.figure(figsize = (16,9))
    plt.plot(globals()[i][['Time[us]']], globals()[i][['Voltage[mV]']], marker = 'x')
    plt.xlabel('Time[us]', fontsize= 25)                             # x축 라벨 설정
    plt.xticks(fontsize = 25)                                              # 눈금 폰트 크기 조정
    plt.ylabel('Voltage[mV]', fontsize= 25)                            # y축 라벨 설정
    plt.yticks(np.arange(-0.06, 0.06, 0.01), fontsize = 25) 
    plt.savefig('C:/Users/ADMIN/Desktop/Data/원본 데이터 이미지 파일(plot)/' + i.split('.')[0])


for i in file_path:
    globals()[i] = pd.read_csv(f'C:/Users/ADMIN/Desktop/Data/원본 데이터 Total/{i}')    
    plt.figure(figsize = (16,9))                                          # 그림 사이즈 조정
    plt.scatter(globals()[i][['Time[us]']], globals()[i][['Voltage[mV]']], marker = 'x')           # 산점도 그리기
    plt.xlabel('Time[us]', fontsize= 25)                             # x축 라벨 설정
    plt.xticks(fontsize = 25)                                              # 눈금 폰트 크기 조정
    plt.ylabel('Voltage[mV]', fontsize= 25)                            # y축 라벨 설정
    plt.yticks(np.arange(-0.06, 0.06, 0.01), fontsize = 25)                                              # 눈금 폰트 크기 조정
    plt.savefig('C:/Users/ADMIN/Desktop/Data/원본 데이터 이미지 파일(산점도)/' + i.split('.')[0])

#--------------------------------------------------------------------------------------------------------


