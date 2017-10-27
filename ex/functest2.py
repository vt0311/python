'''
Created on 2017. 10. 27.

@author: acorn
'''
def oper(first, second):
    result = 2 * first + 3 * second + 5
    return result 

a = 3
b = 4
result = oper(a, b)

print('결과1:', result)

a = 2
b = 3
result = oper(a, b)

print('결과2:', result)

a = 4
b = 1
result = oper(a, b)

print('결과3:', result)