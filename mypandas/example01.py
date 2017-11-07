'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd

# 경로

print('# read_csv를 이용하여 DataFrame 형식으로 불러오기')
moviefile = 'movie.csv'


dfmovie = pd.read_csv(moviefile)
# type : 데이터 타입을 알려주는 함수
print(type(dfmovie))
print(dfmovie)
                      
# index_col : 명시한 컬럼을 색인으로 사용하겠다.                      
dfmovie = pd.read_csv(moviefile, index_col='id')

print('------------------------------')
print('#영화 목록 보여 주기')
print(dfmovie)
print('------------------------------')

print('무슨 타입인가?', type(dfmovie))
print('------------------------------')

print('\n인덱스 내용 확인')
print(dfmovie.index)
print('------------------------------')

print('\n컬럼 내용 확인')
print(dfmovie.columns)

print('------------------------------')

