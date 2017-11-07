'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd

# 엑셀 파일에 행제목이 존재하지 않는 경우
thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt'] # 제목으로 넣을 컬럼 이름

# header = None : 열머리글이 없습니다.
# name = colnames : 컬럼 이름은 colnames를 사용하겠다.
# read_csv에 대한 옵션 
dfthether = pd.read_csv(thetherfile, names=colnames, header=None)

print(dfthether)
# index 속성을 이용하여 색인 객체를 구함.
print(dfthether.index)
# RangeIndex(start = 0, stop = 15, step =1)
# 0부터 14까지의 숫자를 담고 있는 인덱스

# id 컬럼 (dftheather.id)을 새로운 색인으로 지정하겠다.
# id 컬럼은 그대로 보존된다.
dfthether = dfthether.rename(index=dfthether.id)
print(dfthether.index)
print(dfthether)

print('---------------------------------------------------')
# ['theather', 'cnt'] 컬럼만을 이용하여 새로운 데이터를 만드세요.
dfthether = dfthether.reindex(columns=['theater', 'cnt'])
print(dfthether.index)
print(dfthether)

# 인덱스의 이름을 설정한다.
dfthether.index.name = '호호호'
#dftheather.index.name = 'id'

print('\n 상영관 목록 및 상영 횟수 보여주기')

print(dfthether)

