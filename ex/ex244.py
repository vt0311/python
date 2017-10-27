'''
Created on 2017. 10. 26.

@author: hsw
'''

'''
LIFE is TOO Short 만들기
* 힌트 : for 구문과 if 구문 사용
          짝수번쨰 항은 대문자, 홀수번째 항은 소문자로 변경
        join() 함수를 이용하여 특정 문자열에 다른 문자열을 추가
'''

list1 = ['Life', 'is', 'too', 'short']

for i in range(len(list1)):
    if i % 2 == 0 :
        list1[i] = list1[i].upper()
    else :
        list1[i] = list1[i].lower()

print('join() 함수를 이용하여 문자열 합치기')
result = ' '.join(list1)

print('결과 리스트 :', result)
         