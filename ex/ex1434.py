'''
Created on 2017. 10. 30.

@author: acorn
'''

import re

regex = '\\\\hello'
pattern = re.compile(regex)

mystr = 'hohoho\\hello\\hahaha'

mymatch = pattern.search(mystr)
print( mymatch )

print( '--------------------')

# raw : 원자재의, 가공되지 않은
# Raw String 규칙 : 컴파일해야 하는 정규식이 Raw String 입니다.
# 라고 알려주는 역할

regex = r'\\hello' # \\를 백슬래시 2개라고 생각하고 컴파일하라는 의미
pattern = re.compile(regex)

mystr = 'hohoho\\hello\\hahahah'

mymatch = pattern.search(mystr)
print(mymatch) 
 
