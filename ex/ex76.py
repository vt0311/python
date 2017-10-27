'''
Created on 2017. 10. 26.

@author: hsw
'''

# -*- coding: utf-8 -*-

tuple1 = (1, 2, 3)

print('기존의 tuple1은 사라지고, 새로운 tuple1이 생성된다')
# 4뒤에 반드시 콤마를 붙여라. 그렇지 않으면 문자열로 인식한다.
tuple1 = tuple1 + (4,)

print('튜플 출력하기:', tuple1)

# 단순히 콤마 연결로 튜플을 만들 수 있다.
tuple2 = 1,2,3,4

# 리스트를 이용한 튜플 생성
mylist = [1,2,3,4]
tuple3 = tuple(mylist)

if tuple2 == tuple3 :
    print("동일합니다.")
else :
    print("동일하지 않습니다.")
    
    
# 연산자
tuple4 = (1, 2, 3)
tuple5 = (4, 5, 6)

print('+ 연산자는 2개의 튜플을 합니다.(병합)')
tuple6 = tuple4 + tuple5 
print( tuple6 ) # (1,2,3,4,5,6)

print('*: 튜플을 지정한 정수(곱한 수)만큼 반복')
tuple7 = tuple4 * 3
print(tuple7)

print('튜플의 응용 : swap 기법')
a, b = 10, 20
a, b = b , a

print('a=', a, ', b=', b)

tuple8 = (1,2,3,4,5,6)

print( tuple8[1:3])

print( tuple8[3:])

'''
tuple8을 이용하여 
(2, 3, 5)
tuple9 = ??
'''
t8 = tuple8[1:3]
t9 = tuple8[4:5]
tuple9  = t8 + t9
print('tuple9=', tuple9) 



    
