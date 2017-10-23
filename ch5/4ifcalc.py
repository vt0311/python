'''
Created on 2017. 10. 19.

@author: acorn
'''

'''
실습 - 함수 ch3.5ifcalc 계산기 
'''

def simplePlus(num1, num2):
    return num1 + num2

def simpleMinus(num1, num2):
    return num1 - num2

def simpleMulti(num1, num2):
    return num1 * num2

def simpleDivide(num1, num2):
    return num1 / num2


num1 = int(input('정수 입력 :'))

giho = input('+ - * / 입력 :')

num2 = int(input('정수 입력 :'))

result = 0

if giho == '+':
    result simplePlus(num1, num2) 
    #result simpleMinus(num1, num2)
elif giho == '-':
    #pass
    result simpleMinus(num1, num2)
elif giho == '*':
    #pass
    result simpleMulti(num1, num2)
elif giho == '/':
    #pass
    result simpleDivide(num1, num2)
else:
    print('잘못된 입력입니다. 다시 시도하십시오.')

print( '{a} {b} {c} = {d}'.format(a=num1, b=giho, c=num2, d=result))
    
    
    
    