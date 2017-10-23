'''
Created on 2017. 10. 19.

@author: acorn
'''

memVar = 555

def  memFunc():
        memVar = 'local'
        print(memVar)
        
memFunc()

print(memVar)


