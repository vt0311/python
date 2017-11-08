'''
Created on 2017. 10. 26.

@author: hsw
'''
list1 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

print('list 리스트를 집합 자료형으로 변환')
aSet = set(list1)

print('집합 자료형을 다시 list 지료형으로 변환')
newList = list( aSet)

print('결과 :', newList)

print('-----------------')

set1 = set([1,2,3])
print(set1)

print('\n# add() 함수는 요소 1개를 추가한다.')
set1.add(4)
print(set1)

print('\n# update() 함수는 요소를 여러개 추가한다.')
set1.update([5,6,7])
print(set1)


print('\n# 문자 엘(1)은 2개이지만 중복이 안되므로 1개로 보인다.')
set2 = set('hello')
print(set2)

set3 = set([1, 2, 3, 4])
set4 = set([3, 4, 5, 6])

print('\n교집합')
set5 = set3.intersection(set4)
print(set5)

print('\n합집합')
set6 = set3.union(set4)
print(set6)

print('\n차집합')
set7 = set3.difference(set4)
print(set7)


