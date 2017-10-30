'''
Created on 2017. 10. 30.
정규표현식 06
컴파일에 대한 옵션을 연습하는 예시
@author: acorn
'''

import re

regex = 'a.b'
mystr = 'a\nb' 

print('줄바꿈 문자 무시')

pattern = re.compile(regex)
mymatch = pattern.match(mystr)

print(mymatch)
print()
print('줄바꿈 문자 포함')

pattern = re.compile(regex, re.DOTALL)
mymatch = pattern.match(mystr)

print(mymatch)


print('-------------------------------')

regex = '[a-z]'
mystr = 'PYTHON'

pattern = re.compile(regex)
mymatch = pattern.match(mystr)

print('# 대소문자 따진다.')
print(mymatch)
print()

pattern = re.compile(regex, re.IGNORECASE)

mymatch = pattern.match(mystr)
print('# 대소문자를 무시한다')
print(mymatch)

print('-------------------------------')

regex = '^python\s\w+' #소문자
mystr = '''python one
life is too short
python two hello python three
you need python
python four hohoho
'''

pattern = re.compile(regex)
mymatch = pattern.match(mystr)

print('# 멀티라인 적용이 안된 예제')
print(mymatch)
print()

pattern = re.compile(regex, re.MULTILINE)

mymatch = pattern.findall(mystr)
print('# 멀티라인 적용이 된 예제')
print(mymatch)



