'''
Created on 2017. 10. 20.

@author: acorn
'''
try :
    list1 = []
    
    print(list1[0])
    
    int('abcdefg')
    
    print(3/0)

except IndexError:
    print('IndexError 처리')

except ValueError:
    print('ValueError 처리')
    
except ZeroDivisionError:
    print('ZeroDivisionError 처리')    
    