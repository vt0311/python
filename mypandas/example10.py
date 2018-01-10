'''
Created on 2017. 11. 6.

10. 파일 병합

@author: acorn
'''
import pandas as pd



moviefile = 'movie.csv'
dfmovie = pd.read_csv(moviefile, index_col='id')
# print( dfmovie )
# print( )
##########################################
thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt'] # 제목으로 넣을 컬럼 이름
dfthether = pd.read_csv(thetherfile, names=colnames, header=None)


# 수동으로 지워 줘야 한다. 
dfthether = dfthether.rename(index=dfthether.id)
#print( 'dfthether1:', dfthether )
print()

# reindex를 이용하여 id 컬럼을 제거한다.
dfthether = dfthether.reindex(columns = ['theater', 'cnt'])
#print( 'dfthether2:', dfthether )
# print( )
#######################################
# 양쪽 동일한 색인인 id를 이용하여 조인한다..(페이지 251)
mergedData = pd.merge(dfmovie, dfthether, left_index = True, right_index = True)
print('\n 조인된 데이터의 타입 : ', type(mergedData))
print('\n# 두 테이블 조인')

mergedData = mergedData.sort_index()
print( mergedData )

