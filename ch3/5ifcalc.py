'''
Created on 2017. 10. 19.

@author: acorn
'''
num1 = int(input('정수 입력:'))

giho = input(' + - * / 입력:')

num2 = int(input('정수 입력:'))

num3 = 0

if giho == '+':
    #pass
    num3 = num1 +  num2

elif giho == '-':
    #pass
    num3 = num1 - num2

elif giho == '*':
    #pass
    num3 = num1 * num2

elif giho == '/':
    #pass
    num3 = num1 / num2
    
else :
    print('wrong input')
    
    
print('{} {} {} = {}'.format(num1, giho, num2, num3))
    
    