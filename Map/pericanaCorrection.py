import pandas as pd

filename = 'pericana.csv'

pericana_table = pd.read_csv(filename, encoding='cp949', index_col=0, header=0)

# print(pericana_table)

print(pericana_table.sido.unique())
# 특이한 데이터 : ' ', '테스트', '00'

print('\n삭제전')
print(pericana_table[pericana_table['sido'] == '00'])

# 1418은 인덱스 번호이다. 행당 인덱스를 삭제한다.(데이터 베이스 delete 구문) 
pericana_table = pericana_table.drop(pericana_table.index[1418])
  
print('\n삭제후')
print(pericana_table[pericana_table['sido'] == '00'])

print('\n삭제전')
print(pericana_table[pericana_table['sido'] == '테스트'])

# 1046은 인덱스 번호이다
pericana_table = pericana_table.drop(pericana_table.index[1046])
  
print('\n삭제후')
print(pericana_table[pericana_table['sido'] == '테스트'])

print('\nsido가 "스페이스 1칸"으로 되어 있는 행은 지사(지점) 정보이다.')
print( pericana_table[pericana_table['sido'] == ' '])

print('\n지사(지점)들은 걸러 준다.')
pericana_table = pericana_table[pericana_table.sido != ' ']

print('\n시도 unique 테스트') 
print(pericana_table.sido.unique())

sido_table = pd.read_csv('district.csv', encoding='utf-8')

# # print( '\n시도 테이블' )
# # print( sido_table )
# 
# 양쪽 모두 'sido', 'gungu' 컬럼이 존재한다.
m = pd.merge(pericana_table, sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
# print( '\n머지된 결과' )
# print( m )

m_result = m.query('_merge == "left_only"')
# print( '\n좌측에만 있는 행' ) # 교재 259 참조
# print( m_result[['sido', 'gungu']] )
 
                
myfile2 = open('gungu_alias.txt', 'r', encoding='utf-8')
linelists = myfile2.readlines()

gungu_dict = {}
for oneline in linelists:
    mydata = oneline.replace('\n', '').split(':')
    gungu_dict[ mydata[0] ] = mydata[1]
    
print( '\n사전 출력하기' )
print( gungu_dict )

pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v, v))
  
m = pd.merge(pericana_table, sido_table, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
  
m_result = m.query('_merge == "left_only"')
  
print( '\n좌측에만 있는 행' )
print( m_result[['sido', 'gungu']] )
 
m.to_csv('pericana_modify.csv', encoding='cp949', mode='w', index=True)
 
print('파일 저장 완료')