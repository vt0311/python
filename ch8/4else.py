'''
Created on 2017. 10. 20.

@author: acorn
'''

try:
    int('123456')

except ValueError:
    print('ValueError 처리')

else :
    print('예외 없으면 수행')
    
    
