import pandas as pd

filename = 'bbqmini.csv'
atable = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)
print( '\n비비큐 테이블' )
print(atable)

filename = 'districtmini.csv'
btable = pd.read_csv(filename, encoding='utf-8', header=0)
print( '\n행정 구역 테이블' )
print(btable)

# 양쪽 모두 'sido', 'gungu' 컬럼이 존재한다.
m = pd.merge(atable, btable, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
print( '\n머지된 결과' )
print( m )

# _merge 컬럼이 "left_only"인 항목들을 조회
m_result = m.query('_merge == "left_only"')
print( '\n좌측에만 있는 행' )
print( m_result )