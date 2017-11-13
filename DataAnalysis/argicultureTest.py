import pandas as pd 
import json
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

db = json.load(open('foods-2011-10-03.json'))
print( '항목 갯수 :', len(db) ) 
print( '0번째 요소 :', db[0] )
print( '키 목록 :', db[0].keys() )
print( '0번째 요소 영양소 리스트 : ', db[0]['nutrients'][0] )

nutrients = DataFrame(db[0]['nutrients'])
 
# print( nutrients[:7])
info_keys = ['description', 'group', 'id', 'manufacturer']
print('\n컬럼의 순서를 다시 지정하겠다')
info = DataFrame(db, columns=info_keys)

print( info[:5])

print('\ninfo() 함수는 요약한 내용을 이용하여 간단히 보여 주는 함수이다.')
print( info.info())

print('\nvalue_counts() 함수는 도수를 계산하여 역순으로 보여 주는 함수이다.')
print( pd.value_counts(info.group)[:10])

nutrients = [] # 음식들의 영양소 정보를 담을 리스트
for rec in db :
    fnuts = DataFrame(rec['nutrients'])
    # 음식을 위한 id 컬럼 추가하기
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

# print( nutrients ) # 좀 오래 걸린다

print('\n이전에 존재하던 색인은 무시하고, 새로운 색인을 생성하도록 한다.')     
nutrients = pd.concat(nutrients, ignore_index=True)

print('\n중복된 데이터가 있으면 제거하도록 한다.')
nutrients.duplicated().sum()
nutrients = nutrients.drop_duplicates()

print('\n컬럼 이름을 매핑해준다.')
col_mapping = {'description':'food', 'group':'fgroup' }
info = info.rename(columns=col_mapping, copy=False)
print('info 객체 정보 보기')
print( info.info())

col_mapping = {'description':'nutrient', 'group':'nutgroup' }
nutrients = nutrients.rename(columns=col_mapping, copy=False)
print('\nnutrients 객체 정보 보기')
print( nutrients.info())

ndata = pd.merge(nutrients, info, on='id', how='outer')
print('\nndata 객체 정보 보기')
print( ndata.info())
print( ndata.ix[3000] )

result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.savefig('aaa.png', dpi=400)
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])
get_maximum = lambda x : x.xs(x.value.idxmax())
get_minumum = lambda x : x.xs(x.value.idxmin())
max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]

max_foods.foood = max_foods.food.str[:50]
print( max_foods.ix['Amino Acids']['food'] )
print('작업 완료')