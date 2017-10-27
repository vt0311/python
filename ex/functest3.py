'''
Created on 2017. 10. 27.

@author: acorn
'''
def oper2(first, second): # 형식 매개 변수
    result = first ** 2 + second **2
    return result 

a = 3
b = 4
result = oper2(a, b) # 실 매개변수

print('결과1:', result)

a = 2
b = 3
result = oper2(a, b)

print('결과2:', result)

a = 4
b = 1
result = oper2(a, b)

print('결과3:', result)