'''
Created on 2017. 11. 2.

@author: acorn
'''
from konlpy.tag import Twitter
from collections import Counter

mylist = ['탄핵 호호 아버지', '대통령 탄핵 하하', '아버지 탄핵']

message = ''
for item in mylist :
    message += item
    
nlp = Twitter()

mynoun = nlp.nouns(message)

result = Counter( mynoun )

print( result )
