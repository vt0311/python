'''
Created on 2017. 11. 6.

@author: acorn
'''

import pandas as pd


thetherfile = 'thether.csv'

colnames = ['id', 'theater', 'cnt']
# 제목으로 넣을 컬럼 이름

dfthether = pd.read_csv(thetherfile, names= colnames, header=None)
dfthether = dfthether.rename(index=dfthether.id)
dfthether = dfthether.reindex(columns=['theater', 'cnt'])
dfthether.index.name = 'id'
#print( dfthether)
#print()

# 극장별('theater') 상영 횟수('cnt') 집계
mygrouping = dfthether.groupby('theater')['cnt']
sumrSeries = mygrouping.sum()
meanSeries = mygrouping.mean() #평균
sizeSeries = mygrouping.size()

# Series 3개를 이용하여 DataFrame을 만들어낸다.
newAggData = pd.concat([sumrSeries, meanSeries, sizeSeries], axis=1)

print(newAggData)