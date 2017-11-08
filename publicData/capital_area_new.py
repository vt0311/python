import matplotlib.pyplot as plt
import csv
import pandas as pd
from pandas import DataFrame

# 경로 없이 적으면 동일 폴더로 이해한다.
# DataFrame : 엑셀이나 데이터 베이스의 테이블과 동일한 개념
# 파일이 쉼표로 구분이 되어 있으므로 DataFrame으로 불러 올 수 있다.
import sys

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']

filename = 'capital_area.csv'

# sep : 구분자로 무엇을 쓸것인지
myframe = pd.read_table( filename,  sep='|', header=None, names=mycolumn)
print( type(myframe) ) # <class 'pandas.core.frame.DataFrame'>
print()

print( myframe )
print()

print('# 영업소코드 별로 총교통량의 누적 합')
mygrouping = myframe.groupby('영업소코드')['총교통량']
result = mygrouping.sum()

print(result)
print()

print(max(myframe['1종교통량']))

print('# 집계 일자와 집계 시간을 기준으로 총 교통량의 합계')
# mygrouping = myframe.groupby(['집계일자', '집계시'])['총교통량']
mygrouping = myframe.groupby(['집계일자'])['총교통량']
result = mygrouping.sum()

# print(type(result))
print(result)
print()
# x 축 하단에 놓이는 내용
result.index.name = 'Total Traffiic'

myylim = [500000, result.max() + 5 ] # y축의 상하한값
mytitle = 'Chart Title'
# myxticks = ['a', 'b', 'c']
mycolor = 'blue'
myalpha = 0.7

result.plot( kind='line',  color = mycolor, title= mytitle, legend = False, \
                 rot = 15, ylim = myylim, grid=True, alpha = myalpha)

filename = 'capital_area_chart.png'
plt.savefig( filename, dpi=400, bbox_inches='tight')
plt.show()