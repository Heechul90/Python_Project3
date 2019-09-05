# 모듈 준비하기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

raw_data = pd.read_excel('Data/고령운전자와 비고령운전자 교통사고 추세.xlsx',
                         encoding = 'euc-kr')
raw_data

data = raw_data.copy()
data = data.set_index('년도')
data['발생건수(65세 미만)비율'] = (data['발생건수(65세 미만)'] / data['발생건수(합계)'] * 100).round(1)
data['사망자수(65세 미만)비율'] = (data['사망자수(65세 미만)'] / data['사망자수(합계)'] * 100).round(1)
data['부상자수(65세 미만)비율'] = (data['부상자수(65세 미만)'] / data['부상자수(합계)'] * 100).round(1)
data.columns
del data['발생건수(미분류)']
del data['사망자수(미분류)']
del data['부상자수(미분류)']
del data['발생건수(합계)']
del data['사망자수(합계)']
del data['부상자수(합계)']

data.columns
data

plt.subplot(131)
data['발생건수(65세 미만)비율'].plot(kind = 'bar')
plt.subplot(132)
data['사망자수(65세 미만)비율'].plot(kind = 'bar')
plt.subplot(133)
data['부상자수(65세 미만)비율'].plot(kind = 'bar')

plt.plot(data['발생건수(65세 미만)비율'], type = 'bar')