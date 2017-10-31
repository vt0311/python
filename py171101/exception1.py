'''
Created on 2017. 10. 31.

0으로 나누기(예외 처리)

@author: acorn
'''

x = 4
y = 0

list1 = [1, 2, 3]

try:
    z = x / y
    print(list1[4])

except ZeroDivisionError  as err:
    pass # pass는 오류를 발생시키지 않고 그냥 통과한다.
