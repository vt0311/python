'''
Created on 2017. 10. 30.

@author: acorn
'''

import re

mylist = ['acccb', 'a...b', 'aaab', 'a.cccb']

# a와 b 사이에 점 문자가 최소 3개 이상인 항목들
regex = 'a[.]{3,}b'
pattern = re.compile(regex)

for item in mylist :
    if pattern.match(item) :
        print('패턴', item, ': True')
    else :
        print('패턴', item, ': False')
        
print('---------------------------')

# *의 의미는 바로 앞의 문자가 0번 이상 반복되어야 함을 의미한다.
regex2 = 'ca*t' # c와 t 사이에 a가 0번 이상
pattern2 = re.compile(regex2)

mylist2 = ['cat', 'ct', 'caaaat']
for item in mylist2 :
    if pattern2.match(item) :
        print('패턴', item, ': True')
    else :
        print('패턴', item, ': False')