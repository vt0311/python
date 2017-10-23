'''
Created on 2017. 10. 23.

@author: acorn
'''

with open('test1.txt', 'r') as file3:
    str = file3.read()
    print(str)
    '''file3.close()
    with open은 자동 close됨.
    '''
    
print('close - file read')