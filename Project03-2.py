# 모듈 준비하기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

raw_data = pd.read_excel('Data/05. population_raw_data.xlsx',
                         header = 1)
raw_data
data = raw_data.copy()


data.fillna(method = 'pad', inplace = True)
data.rename(columns = {'행정구역(동읍면)별(1)' : '광역시도',
                       '행정구역(동읍면)별(2)' : '시도',
                       '계' : '인구수'},
            inplace = True)
data = data[(data['시도'] != '소계')]
data.is_copy = False

data.rename(columns = {'항목' : '구분'},
            inplace = True)
data.loc[data['구분'] == '총인구수 (명)', '구분'] ='합계'
data.loc[data['구분'] == '남자인구수 (명)', '구분'] ='남자'
data.loc[data['구분'] == '여자인구수 (명)', '구분'] ='여자'

data['20-39세'] = data['20 - 24세'] + data['25 - 29세'] + data['30 - 34세'] + data['35 - 39세']
data['65세이상'] = data['65 - 69세'] + data['70 - 74세'] + data['75 - 79세'] + data['80 - 84세'] + data['85 - 89세'] + data['90 - 94세'] + data['95 - 99세'] + data['100+']

data2 = data.copy()

data2 = pd.pivot_table(data2,
                       index = ['광역시도', '시도'],
                       columns = ['구분'],
                       values = ['인구수', '20-39세', '65세이상'])

data2['소멸비율'] = data2['20-39세', '여자'] / (data2['65세이상', '합계'] / 2)

data2['소멸위기지역'] = data2['소멸비율'] < 1.0

data2[data2['소멸위기지역'] == True].index.get_level_values(1)

data2.reset_index(inplace = True)
data2

tmp_columns = [data2.columns.get_level_values(0)[n] + data2.columns.get_level_values(1)[n]
               for n in range(0, len(data2.columns.get_level_values(0)))]
data2.columns = tmp_columns
data2.info()
data2

data2.to_csv('Data/인구소멸위기지역.csv',
             encoding = 'euc-kr',
             sep = ',')