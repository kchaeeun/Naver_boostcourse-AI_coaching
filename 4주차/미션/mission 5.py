import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(3)
names=['group_a','group_b','group_c']
values = [1,10,100]

plt.figure(figsize=(9,3)) #전체크기를 의미

plt.subplot(1,3,1) #먼저 그래프의 위치 선정(plt.subplot(nrow, ncolumn, index)
plt.bar(names, values) #막대그래프

plt.subplot(1,3,2)
plt.plot(names, values,'o') #원으로된 그래프

plt.subplot(1,3,3)
plt.plot(names, values) #실선 그래프

plt.show()   #pandas내에도 matplotlib이 있기 때문에 pandas만 import해줘도 실현화 시킬 수 있음 (ex. pd.plt) rkm