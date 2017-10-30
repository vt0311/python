'''
Created on 2017. 10. 27.

@author: acorn
'''
# 일반 함수를 사용하는 경우
def two_times1(numList):
    result = []
    for num in numList:
        result.append(num * 2)
        
    return result

list1 = [1, 2, 3]
result = two_times1(list1)

#print(result)

# map 함수를 사용하는 경우
def two_times2(number):
    return 2 * number

list1 = [3, 4, 5]
list2 = list(map(lambda a: 2*a, list1))

#print(list2)



# lambda 와 map 함수를 같이 사용하기
list1 = [4, 5, 6]
list3 = list(map(lambda a : 2 * a, list1))

#print(list3)


# 추가 문제 : 
# map 함수를 사용하는 경우
mylist = [2, 3, 4]
# map 함수를 이용하여 mylist의 요소값들을 
# 3제곱하는 프로그램을 만드세요.
# [2, 3, 4]즌 [8, 27, 64]가 출력된다.

mylist2 = list(map(lambda a : a**3 , mylist))
print('mylist2:',mylist2)

