'''
Created on 2017. 11. 3.

@author: acorn
'''
from pandas import DataFrame

# 표를 만들기 위한 데이터 사전
sdata = {'city' : ['서울', '서울', '서울', '부산', '부산'],\
         'year' : [2000, 2001, 2002, 2001, 2002],\
         'pop' : [1.5, 1.7, 3.6, 2.4, 2.9]}

mycolumn = ['city', 'year', 'pop'] #컬럼

myindex = ['one', 'two', 'three', 'four', 'five'] #색인

myframe = DataFrame(sdata, columns = mycolumn, index=myindex)

print(myframe)