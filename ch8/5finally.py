'''
Created on 2017. 10. 20.

@author: acorn
'''

try :
    print(3/0)
    
except ZeroDivisionError:
    print('ZeroDivisionError 처리')
 
else :
    print('no exception')
    
finally:
    print('always execute')        