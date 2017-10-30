'''
Created on 2017. 10. 30.

@author: acorn
'''
import re 

mylist = ['a1b2', '1a2b']

# a부터 d 사이의 임의의 문자가 1번 이상 반복

regex = '[a-d]+'
pattern = re.compile(regex)


# match 메소드는 문자열의 처음부터 검사한다.
# 따라서 1a2b는 처음이 숫자이므로 False이다.

for item in mylist :
    if pattern.match(item) :
        print('match 메소드', item, ': True')
    
    else :
        print('match 메소드', item, ': False')
        
      
for item in mylist :
    if pattern.search(item):
        print('search 메소드', item, ': True')
    else :
        print('search 메소드', item, ': False')           
        