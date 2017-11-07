'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd

moviefile = 'movie.csv'

dfmovie = pd.read_csv(moviefile, index_col='id')

# 그룹핑 : 페이지 352
print('# 장르별 영화 개수')

# 'genre'로 그룹핑한 다음, ['title']에 대해서...
mygrouping = dfmovie.groupby('genre')['title']
sumresult3 = mygrouping.count()
print(sumresult3)

print(type(sumresult3))
print()