'''
Created on 2017. 10. 26.

@author: acorn
'''
lists = ['강감찬', '김유신']
print('\n# 출력1')
print(lists)

print('# append 함수를 이용하여 마지막 위치에 요소를 추가한다.')
lists.append('이순신')
lists.append('이성계')
print(lists)

print('# 0번째 요소 가져오기 : {}'.format(lists[0]))

# len(lists)는 요소의 갯수를 알려준다.
print('# 마지막 요소 가져오기 : {}'.format(lists[len(lists)-1]))

print('\n# 슬라이싱')
print('# 1번째부터 2번째 요소까지 슬라이싱')
print( lists[1:3] )

print('\n# lists는 타입에 구애받지 않고, 무엇이든지  저장 가능하다.')
anydata = [10, '가가', 12.34, [10, 20, 30]]
print(anydata)