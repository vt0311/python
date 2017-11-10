import pandas as pd 

filename = 'nene.csv'

nene_table = pd.read_csv(filename, encoding='cp949', index_col=0, header=0)

# print( '\n보정전 결과' )
# print(nene_table.sido.unique())

# 축약된 형식을 정식 명칭으로 변경한다.
# 예시 : 광주 --> 광주광역시
myfile2 = open('sido_alias.txt', 'r', encoding='utf-8')
linelists = myfile2.readlines()

sido_dict = {}
for oneline in linelists:
    mydata = oneline.replace('\n', '').split(':')
    sido_dict[ mydata[0] ] = mydata[1]

# sido 컬럼 보정 완료
nene_table.sido = nene_table.sido.apply(lambda v : sido_dict.get(v, v))

# print( '\n보정후 결과' )
# print(nene_table.sido.unique())

sido_table = pd.read_csv('district.csv', encoding='utf-8')

m = pd.merge(nene_table, sido_table, on=['sido', 'gungu'], \
             how='outer', suffixes=['', '_'], indicator=True)

print( '\n머지된 결과' )
print( m )

m_result = m.query('_merge == "left_only"')
print( '\n좌측에만 있는 행' )
print( m_result[['sido', 'gungu']] )

gungu_alias = '''여주군:여주시 당진군:당진시'''

gungu_dict= dict(aliasset.split(':') for aliasset in gungu_alias.split())

nene_table.gungu = nene_table.gungu.apply(lambda v : gungu_dict.get(v, v))

print( '\n특이한 데이터' )
print(nene_table[(nene_table['sido']=='경상북도') & (nene_table['gungu']=='남구')])

nene_table.loc[(nene_table['sido']=='경상북도') & (nene_table['gungu']=='남구'), 'gungu'] = '포항시'

# '경상북도', '남구'인 데이터는 495 인덱스를 가진고 있다.
print( '\n특이한 데이터 확인하기' )
print(nene_table.loc[495])

m = pd.merge(nene_table, sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
 
m_result = m.query('_merge == "left_only"')
 
print( '\n좌측에만 있는 행' )
print( m_result[['sido', 'gungu']] )

m.to_csv('nene_modify.csv', encoding='utf-8', mode='w', index=True)

print('파일 저장 완료')