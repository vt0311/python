'''
Created on 2017. 10. 30.

@author: acorn
'''
import re

regex = '[a-z]+'
pattern = re.compile(regex)

mystr = 'python'

mymatch = pattern.match(mystr)

print(mymatch.group())

# match 메소드는 상상 문자열의 시작부터 조사하기 때문에 
# start는 항상 0 이다.
print(mymatch.start())
print(mymatch.end())
# 시점과 종점 인덱스의 튜플을 반환
print(mymatch.span())


print('----------------')

mystr = "3 python"
mysearch = pattern.search(mystr)

print(mysearch.group())


# search 메소드 사용시 start()는 값이 다르게 나올 수 있다.
print(mysearch.start())
print(mymatch.end())
print(mymatch.span())
