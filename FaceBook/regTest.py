import re

print('전화 번호 검사')

regExp = '^\d{3}-\d{3,4}-\d{4}$'

print( bool(re.search(regExp, '010-111-1234')))
print( bool(re.search(regExp, 'aa010-111-1234가가')))
print( bool(re.search(regExp, '0101111234')))