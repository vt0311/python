import pandas as pd
import numpy as np

mynames = ['name', 'sex', 'births']

names1880 = pd.read_csv('names/yob1880.txt', names = mynames)
print('\nyob1880.txt : 연도별로 최소 5명 이상 중복되는 이름만 포함하고 있다.')
print( names1880 )

print('\n전체 출생수 : 성별 출생수를 모두 합한 값')
mygrouping = names1880.groupby('sex')
result = mygrouping.sum()
print( result )

# names 폴더에 파일이 매우 많이 들어 있다.
years = range( 1880, 2016)
pieces = []
columns = ['name', 'sex', 'births']

for year in years :
    path = 'names/yob%d.txt' % ( year )
    frame = pd.read_csv( path, names = columns )
    frame['year'] = year # 새로운 컬럼 year을 추가한다.
    pieces.append( frame )
    
# ignore_index=True : 이전에 사용되던 색인은 무시하고, 그냥 숫자형 색인을 만들어라.

names = pd.concat(pieces, ignore_index=True)    
print('\n전체 데이터')
print( names )

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print('\n가장 끝의 5개만 조회')
print( total_births.tail() )
print( type(total_births) )
total_births.plot(title='Total births by sex and year')

import matplotlib.pyplot as plt
plt.savefig('연도별 성별 추이 그래프.png', dpi=400) 
# plt.show()

# prop 컬럼 추가 : 전체 출생수에서 차지하는 비율이라고 가정한다.
# 우선 함수 하나 만들기
def add_prop(group):
    births = group.births.astype( float )
    group['prop'] = births / births.sum()
    return group 

names = names.groupby(['year', 'sex']).apply(add_prop)
print('\nprop 컬럼 추가된 전체 데이터')
print( names )

print('\n년도별 성별에 따른 빈도수가 가장 높은 것 1000개')
# 우선 함수 하나 만들기
def get_top1000(group):    
    return group.sort_values(by='births', ascending=False)[:1000] 

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))
print( top1000 )

print('\n이름 유행 분석')
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

print('\n특정 이름들의 년도별 간단한 추이 살펴 보기')

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
print('요약 정보 간단히 보기')
print( total_births.info() )

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')

# 그래프를 보게 되면 예로 든 4명은 최근에 인기가 없는 이름이라고 볼 수 있다.
plt.savefig('4명에 대한 그래프.png', dpi=400)
 
# plt.show()
print('\n인기 있는 이름 1000개가 차지하는 퍼센트 확인')
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop year and sex',\
           yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
plt.savefig('상위 1000개의 이름.png', dpi=400)
print('그래프를 보면 상위 1000개의 전체 비율이 지속적으로 낮아지고 있다.')
print('그래프를 보면 실제로 이름의 다양성이 높아지고 있음을 볼 수 있다.')

# 마지막 글자의 변화
get_last_letter = lambda x : x[-1]

last_letters = names.name.map(get_last_letter)

print('name 열에서 마지막 글자를 추출한다.')
print( last_letters.head() )
last_letters.name = 'last_letter'
table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)

print('전체 기간중에서 3개[1910, 1960, 2010]의 지점을 골라서 마지막 글자 몇 개를 출력해보자')
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
print( subtable.head() )

print('비율을 계산하기 위하여 전체 출생수로 나눈다.')
print( subtable.sum() )
letter_prop = subtable / subtable.sum().astype(float)
print( letter_prop )

print('\n마지막 글자 비율은 성별, 연도별 막대 그래프로 그리기')
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
plt.savefig('남녀 이름에서 마지막 글자의 빈도.png', dpi=400)