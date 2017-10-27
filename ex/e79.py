'''
Created on 2017. 10. 26.

@author: hsw
'''

mydict = {'김철수': 35 , '박영희': 50, '홍길동':40}
print('사전 내역 :', mydict )

print('\nkeys() : 사전의 key 리스트를 보여 준다.')
for key in mydict.keys():
    print(key)

print('\nvalues() : 사전의 value 리스트를 보여준다.')
for value in mydict.values():
    print(value)
    
print('\nkeys()를 이용한 value 검색하기')
for key in mydict.keys():
    print('{}의 나이는 {}입니다.'.format(key, mydict[key]))

'''
'''   
print('\nitems() : key와 value로 이루어진 쌍(pair)을 보여준다.')
for key, value in mydict.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
    
print('\nin은 키의 존재 여부를 확인해준다.')
findKey = '심형래'
if findKey in mydict :
    print(findKey + '는 존재 합니다.')
else:
    print(findKey + '는 존재하지 않습니다.')