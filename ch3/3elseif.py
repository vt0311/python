'''
Created on 2017. 10. 19.

@author: acorn
'''
from builtins import int

intV = int(input('정수입력: '))

if intV < 100:
    if intV < 50:
        
        if intV < 0:
            print('음수')
        else :
            print('50보다 작은 정수')
            
    else:
        print('100보다 작고 50보다 큰 양수')
else:
    print('100보다 큰 양수')        
