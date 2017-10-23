'''
Created on 2017. 10. 19.

@author: acorn
'''

import random
from random import choice

myInt = int(input('선택(1: 가위, 2:바위, 3:보) : '))

print('{}을 선택하였습니다.'.format(myInt))
#print(random.choices(['가위, 바위, 보']))

computer = random.choices([1, 2, 3])

print('컴퓨터의 선택:{}'.format(computer))

if myInt == 0 :
         break

else :
    if myInt == computer[0]:
        print('비겼습니다.')
    elif myInt == 1 :
        if computer[0] == 3:
            print('승리 하였습니다.')
        if computer[0] == 2:
            print('패배하였습니다.')
        if computer[0] == 1:
            print('비겼습니다.')    
            
    elif myInt == 2 :
        if computer[0] == 3:
            print('승리 하였습니다.')
        if computer[0] == 2:
            print('패배하였습니다.')
        if computer[0] == 1:
            print('비겼습니다.') 
            
    elif myInt == 3 :
        if computer[0] == 3:
            print('승리 하였습니다.')
        if computer[0] == 2:
            print('패배하였습니다.')
        if computer[0] == 1:
            print('비겼습니다.')                 
'''
if (  == 3) {
    print('승리하셨습니다.')
    } 
'''

#if ( )


