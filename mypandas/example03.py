'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd
import numpytest as np
from pandas.core.frame import DataFrame

moviefile = 'movie.csv'

dfmovie = pd.read_csv(moviefile, index_col='id')

# 장르가 코미디인 항목만 조회
newdata1 = dfmovie[dfmovie.genre == '코미디']
print( newdata1)
print()

# 감독 이름이 존재하는 항목만 조회
# notnull 메소드는 isnull의 상반되는 메소드이다.
newdata2 = dfmovie[ pd.notnull(dfmovie.director)]

print(newdata2)
print()


# 배우 이름이 존재하는 항목의 제목과 배우 이름만 조회
newdata3 = dfmovie[pd.notnull(dfmovie['actor'])]


column3 = ['title', 'actor']
# DataFrame에 대한 reindex는 색인, 컬럼 둘다 변경이 가능
newdata3 = newdata3.reindex(columns = column3)

print(newdata3)
print()
