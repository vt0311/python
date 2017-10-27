'''
Created on 2017. 10. 27.

@author: acorn
'''
mylist1 = ['토니안', '김건모', '허지웅', '박수홍', '김제동']

print('\nidx는 인덱스, value는 값이다.')
for idx, value in enumerate(mylist1):
    print('{}번째 값 : {}'.format(idx, value))
    
print('\nin은 키의 존재 여부를 확인해준다.')
for a in enumerate(mylist1):
    print('{}번째 값 : {}'.format(a[0], a[1]))
    
print('*을 이용한 방법')
for a in enumerate(mylist1):
    print('{}번째 값 : {}'.format(*a))
    
ages = {'김철수':35, '박영희':60, '홍길동':10}
print('\nitems()는 키와 값으로 이루어진 쌍(pair)을 보여준다.')
for key, val in ages.items():
    print('{}의 나이는 {}'.format(key, val))
    
    
    
    
