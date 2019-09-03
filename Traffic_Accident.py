import numpy as np
import pandas as pd

raw_data = pd.read_csv('Data/연령층별 노인 사상자.csv',
                       encoding = 'euc-kr')
raw_data.head()

data = raw_data.copy()
data.head()

len(data)
data['시도'][1]

for i in range(len(data)):
    if data['시도'][i] == '합계':
        data = data.drop([i])

data = data.drop([497])
data = data.drop([3, 4])
data.head()

data.to_csv('Data/Traffic_Accident(age).csv',
            encoding = 'euc-kr',
            index = False,
            sep = ',')

data1 = pd.read_csv('Data/Traffic_Accident(age).csv',
                       encoding = 'euc-kr')
data1.head()


from matplotlib import pyplot as plt

plt.plot()
data1['2014']