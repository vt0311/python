'''
Created on 2017. 11. 6.

1. 회원 데이터를 DataFrame으로 만든다.
단, '신사임당'은 목록에서 제외한다.

2. 급여가 300원 이상인 사람만 조회해 보세요.
이 데이터를 이용하여 수평 막대 그래프를 그려라.

3. 게시물 데이터를 DataFrame으로 만들어라

4. 게시물을 남긴 사람들의 이름, 성별, 제목, 내용을
    DataFrame으로 만들라.
    
5. 성별 급여의 총합을 pie 그래프로 만들라.

@author: acorn
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


plt.rc('font', family='Malgun Gothic')

boardfile = 'board.csv'

dfboard = pd.read_csv(boardfile, index_col='no')

#print(type(dfboard))
print(dfboard)

memberfile = 'member.csv'

colnames = ['id', 'name', 'salary', 'gender']

# header= None : 열머리글이 없다.
# names = colnames : 컬럼이름은 colnames 사용

#dfmember = pd.read_csv(memberfile, index_col='id')
dfmember = pd.read_csv(memberfile, names=colnames, header=None)
groupbyData = dfmember.groupby('name')['salary']

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels : 원주 외곽에 보여줄 라벨
labels = []

# chartData : 그래프에 표시될 값
chartData = groupbyData.sum()
#print(type(chartData))
print(chartData)


# 수동으로 지워 줘야 한다.
dfmember = dfmember.rename(index = dfmember.id)

# reindex를 이용하여 id 컬럼을 제거한다.
dfmember = dfmember.reindex(columns=['name', 'gender'] )

#dfmember.index.name = 'id'
#groupbyData = dfmember.groupby()

#meanSeries = groupbyData.sum()
print('dfmember:', dfmember)
# index 속성을 이용하여 색인 객체를 구함.
print('dfmember.index:', dfmember.index)
#RangeIndex(Start = 0, stop = 5, step=1)
# 0부터 5까지의 숫자를 담고 있는 인덱스
print('-----------------------')
# id 컬럼을 새로운 색인 으로 지정한다.
# id 컬럼은 그대로 보존된다.
#dfmember = dfmember.rename(index=dfmember.id)
#print(dfmember.index)
#print()
print(dfmember)
#print('================================')

# 1.신사임당을 제외한 목록 가져오기
#newdata1 = dfmember[dfmember.name != '신사임당']
#print( newdata1)
print()

print('================================')

# 2. 급여데이터가 300 이상인 사람만 가져오기,
# 수평막대그래프도 그리기.
#newdata2 = dfmember[dfmember.salary >= 300]
#print(newdata2)
print()

#mygrouping = newdata2.groupby('id')['salary']
#meanSeries = mygrouping.mean()
#print(meanSeries)

#myylim = [0, meanSeries.max() + 5] # y축의 상하한값
#mytitle = '급여 데이터 300이상'

#mycolor = 'yellow'
#myalpha = 0.7

# table = True : 차트에 사용된 데이터를 표 형태로 보여준다.
#meanSeries.plot(kind ='bar', color= mycolor, title = mytitle, legend = True, rot = 15, ylim = myylim, grid=True, alpha = myalpha)
#filename = 'pandatest02.png'
#plt.savefig(filename, dpi=400, bbox_inches='tight') 
#plt.show()

# 3. 게시물 데이터를 DataFrame 으로 만들라.
#boardfile = 'board.csv'
#colnames = ['']
#dfboard = pd.read_csv(boardfile, index_col='no')

#print(type(dfboard))
#print(dfboard)
#print(dfboard.index)
#print(dfboard.columns)

#groupbyData = dfboard.groupby()


# 인덱스의 이름을 설정한다.
#dfmember.index.name = 'id'

# Series 3개를 이용하여 DataFrame을 만든다.
#newAggData = pd.concat([sumrSeries, meanSeries, size])

#print(newAggData)

# 양쪽 동일한 색인인 id를 이용하여 조인한다..(페이지 251)
mergedData = pd.merge(dfmember, dfboard, left_index = True, right_index = True)
#print('\n 조인된 데이터의 타입 : ', type(mergedData))
print('\n# 두 테이블 조인')

mergedData = mergedData.sort_index()
print( mergedData )




