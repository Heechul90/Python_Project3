# 모듈 준비하기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

raw_data = pd.read_excel('Data/시군_시군구별 가해운전자 연령층별 교통사고.xls',
                     encoding = 'euc-kr')
raw_data
raw_data.head()

data = raw_data.copy()
data.head()
data.columns

data = data[['시도', '시군구', '발생년도', '2014.8', '2014.9',
                                        '2015.8', '2015.9',
                                        '2016.8', '2016.9',
                                        '2017.8', '2017.9',
                                        '2018.8', '2018.9',]]
data

for i in range(len(data)):
    if data['시군구'][i] == '합계':
        data = data.drop(i)

data
data = data.drop(0)
data = data.drop(745)

data[data['시군구'].isin(['마산시', '창원시', '진해시'])]
data['시군구'].unique()
data[data['시군구'].isin(['창원시(통합)'])]
data['시군구'][733] = '창원시'
data['시군구'][734] = '창원시'
data['시군구'][735] = '창원시'

data.rename(columns = {'2014.8': '2014 65이상',
                       '2014.9': '2014 70이상',
                       '2015.8': '2015 65이상',
                       '2015.9': '2015 70이상',
                       '2016.8': '2016 65이상',
                       '2016.9': '2016 70이상',
                       '2017.8': '2017 65이상',
                       '2017.9': '2017 70이상',
                       '2018.8': '2018 65이상',
                       '2018.9': '2018 70이상'},
            inplace = True)
data

data.to_csv('Data/도시별 노령운전자 교통사고.csv',
            index = False,
            encoding = 'euc-kr',
            sep = ',')

data1 = pd.read_csv('Data/도시별 노령운전자 교통사고.csv',
                    encoding = 'euc-kr')
data1.fillna(0)

data1['도시'] = data1['시도'] + data1['시군구']
data1

del data1['시도']
del data1['시군구']

cols = data1.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols
data1 = data1[cols]
data1

data1.to_csv('Data/도시별 노령운전자 교통사고2.csv',
             encoding = 'euc-kr',
             sep = ',')

data2 = pd.read_csv('Data/도시별 노령운전자 교통사고2.csv',
                    index_col = 0,
                    encoding = 'euc-kr')
data2

df = pd.DataFrame(columns=['idx', 'number'])
Accident = pd.DataFrame(columns=['도시',
                                 '2014_65_사고', '2014_65_사망', '2014_65_부상',
                                 '2015_65_사고', '2015_65_사망', '2015_65_부상',
                                 '2016_65_사고', '2016_65_사망', '2016_65_부상',
                                 '2017_65_사고', '2017_65_사망', '2017_65_부상',
                                 '2018_65_사고', '2018_65_사망', '2018_65_부상',
                                 ])

for i in range(len(data2)):
    if data2['발생년도'][0] == '사고건수':
        메메메메
    if data2['발생년도'][1] == '사망지수':
        메메메메
    if data2['발생년도'][2] == '부상지수':
        메메메메

