'''
Created on 2017. 11. 6.

06. 극장 / 영화별로 상영 횟수 집계
 
@author: acorn
'''

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.series import Series

# 그래프 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

# 엑셀 파일 읽어 오기
thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt'] #제목으로 넣을 컬럼 이름
dfthether = pd.read_csv(thetherfile, names = colnames, header=None)
print(dfthether)

mygrouping = dfthether.groupby('theater')['cnt']
meanSeries = mygrouping.mean()
print(meanSeries)

myylim = [0, meanSeries.max() + 5] # y축의 상하한값
mytitle = 'showing count per theater'

# myxticks = ['a', 'b', 'c']
mycolor = 'yellow'
myalpha = 0.7

# table = True : 차트에 사용된 데이터를 표 형태로 보여준다.
meanSeries.plot(kind ='bar', color= mycolor, title = mytitle, legend = True, rot = 15, ylim = myylim, grid=True, alpha = myalpha)
filename = 'example06.png'
plt.savefig(filename, dpi=400, bbox_inches='tight') #여기 클릭
plt.show()


        