import numpy as np
import pandas as pd

raw_data = pd.read_excel('Data/가해운전자 연령층별 시군구별 교통사고.xls',
                         encoding = 'euc-kr')
raw_data.head()

data = raw_data.copy()
data.head()
data.columns
data = data[['시도', '시군구', '2014년.7', '2015년.7', '2016년.7', '2017년.7', '2018년.7']]

data.head()

for i in range(len(data)):
    if data['시군구'][i] == '합계':
        data = data.drop(i)
data
data = data.drop(0)
data = data.drop(254)
data = data.drop(255)

data[data['시군구'].isin(['마산시', '창원시', '진해시'])]
data = data.drop(229)
data = data.drop(231)
data = data.drop(232)

data.rename(columns = {'2014년.7': '2014',
                       '2015년.7': '2015',
                       '2016년.7': '2016',
                       '2017년.7': '2017',
                       '2018년.7': '2018',
                       },
            inplace = True)
data

data.to_csv('Data1/시군구별 교통사고.csv',
            encoding = 'euc-kr',
            index = False,
            sep = ',')
