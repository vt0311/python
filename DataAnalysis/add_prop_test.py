import pandas as pd


columns = ['name', 'sex', 'births']

path = 'abcd.txt'
frame = pd.read_csv( path, names = columns )
frame['year'] = 2017 # 새로운 컬럼 year을 추가한다.

print( frame )