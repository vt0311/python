'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mypandas.example05 import meanSeries

# 그래프 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')


thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt']
dfthether = pd.read_csv(thetherfile, names=colnames, header=None)
groupbyData = dfthether.groupby('id')['cnt']


meanSeries = groupbyData.sum()
print(type(meanSeries))
print(meanSeries)

meanSeries = groupbyData.sum()
print(type(meanSeries))
print(meanSeries)

meanSeries.index.name = 'movie name'
myxlim = [0, meanSeries.max() + 5] # y축의 상하한값
mytitle = 'showing count per theater'
mycolor = 'pink'
myalpha = 0.7

# table = True : 차트에 사용된 데이터를 표 형태로 보여준다.
meanSeries.plot(kind='barh', color=mycolor, title=mytitle, legend=True, rot=0, xlim = myxlim, grid= True, alpha = myalpha)

filename = 'example08.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()