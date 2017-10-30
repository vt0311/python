'''
Created on 2017. 10. 30.

@author: acorn
'''

import re

#print('전화 번호 검사')

regExp = '^\d{3}-\d{3,4}-\d{4}$'

#print( bool(re.search(regExp, '010-111-1234')))
#print( bool(re.search(regExp, 'aa010-111-1234가가')))
#print( bool(re.search(regExp, '0101111234')))

postno = 'a12345'
postno2 = '12345'

regExp2 = '^\d{5}$'

print( bool(re.search(regExp2, postno)))
print( bool(re.search(regExp2, postno2)))


