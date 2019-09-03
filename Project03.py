# 모듈 준비하기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

Sido = pd.read_csv('Data1/시군구별 교통사고.csv',
                   encoding = 'euc-kr')
Sido

plt.bar(Sido['시군구'], Sido['2014'])
plt.show()