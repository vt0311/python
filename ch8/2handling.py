'''
Created on 2017. 10. 20.

@author: acorn
'''

list1 = []

try :
    print(list1[0])
except IndexError:
    
    print('예외 처리')   
    
    
try :
    int('abcdefg')
  #  print(list1[0])
except ValueError:
    
    print('예외 처리2')       
    
    
try :
    print(3/0)
except ZeroDivisionError:
    
    print('예외 처리3')       
    
    