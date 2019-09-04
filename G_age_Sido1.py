import numpy as np
import pandas as pd

raw_data = pd.read_excel('Data/가해운전자 연령층별 시군구별 교통사고.xls',
                         encoding = 'euc-kr')
raw_data.head()

data = raw_data.copy()
data.head()
data.columns
data = data[['시도', '시군구', '2014년', '2014년.7', '2015년', '2015년.7', '2016년', '2016년.7', '2017년', '2017년.7', '2018년', '2018년.7']]

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

data.rename(columns = {'2014년': '2014 합계',
                       '2014년.7': '2014',
                       '2015년': '2015 합계',
                       '2015년.7': '2015',
                       '2016년': '2016 합계',
                       '2016년.7': '2016',
                       '2017년': '2017 합계',
                       '2017년.7': '2017',
                       '2018년': '2018 합계',
                       '2018년.7': '2018',
                       },
            inplace = True)
data
data.fillna(0)
data.head()

data['합계'] = data['2014 합계'] + data['2015 합계'] + data['2016 합계'] + data['2017 합계'] + data['2018 합계']
data['고령운전자 사고합계'] = data['2014'] + data['2015'] + data['2016'] + data['2017'] + data['2018']


data.to_csv('Data1/시군구별 교통사고1.csv',
            encoding = 'euc-kr',
            index = False,
            sep = ',')

data1 = pd.read_csv('Data1/시군구별 교통사고1.csv',
                    encoding = 'euc-kr')

data1.head()
data1[data1['시도'].isnull()]
data1[data1['2014'].isin(['0'])]
data1[data1['2015'].isin(['0'])]
data1[data1['2016'].isin(['0'])]
data1[data1['2017'].isin(['0'])]
data1[data1['2018'].isin(['0'])]

data1['2014년 고령운전자 사고비율'] = round(data1['2014'] / data1['2014 합계'] * 100, 2)
data1['2015년 고령운전자 사고비율'] = round(data1['2015'] / data1['2015 합계'] * 100, 2)
data1['2016년 고령운전자 사고비율'] = round(data1['2016'] / data1['2016 합계'] * 100, 2)
data1['2017년 고령운전자 사고비율'] = round(data1['2017'] / data1['2017 합계'] * 100, 2)
data1['2018년 고령운전자 사고비율'] = round(data1['2018'] / data1['2018 합계'] * 100, 2)
data1['5년 고령운전자 사고비율'] = round(data1['고령운전자 사고합계'] / data1['합계'] * 100, 2)
data1.head()

del data1['2014 합계']
del data1['2015 합계']
del data1['2016 합계']
del data1['2017 합계']
del data1['2018 합계']

data1.head()
data1.columns

data1['도시'] = data1['시도'] + data1['시군구']
del data1['시도']
del data1['시군구']
data1['도시'].unique()

cols = data1.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols
data1 = data1[cols]
data1.columns


data1.to_csv('Data1/시군구별 교통사고2.csv',
             encoding = 'euc-kr',
             sep = ',')

data2 = pd.read_csv('Data1/시군구별 교통사고2.csv',
                    index_col = 0,
                    encoding = 'euc-kr')
data2.head()
data2.columns


# 모듈 준비
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 사용하기
from matplotlib import font_manager, rc
import platform
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


# 2014년
data2.sort_values(by = '2014년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '2014년 고령운전자 사고비율', ascending = False).tail(10)

# 2015년
data2.sort_values(by = '2015년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '2015년 고령운전자 사고비율', ascending = False).tail(10)

# 2016년
data2.sort_values(by = '2016년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '2016년 고령운전자 사고비율', ascending = False).tail(10)

# 2017년
data2.sort_values(by = '2017년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '2017년 고령운전자 사고비율', ascending = False).tail(10)

# 2018년
top10_2018 = data2.sort_values(by = '2018년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '2018년 고령운전자 사고비율', ascending = False).tail(10)
top10_2018

sns.barplot(x = top10_2018['도시'],
            y = top10_2018['2018년 고령운전자 사고비율'],
            data = top10_2018)
plt.show()


# 5년
top10 = data2.sort_values(by = '5년 고령운전자 사고비율', ascending = False).head(10)
data2.sort_values(by = '5년 고령운전자 사고비율', ascending = False).tail(10)
top10

## 그래프
sns.barplot(x = top10['도시'],
            y = top10['5년 고령운전자 사고비율'],
            data = top10)
plt.show()