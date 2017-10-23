'''
Created on 2017. 10. 19.

@author: acorn
'''

memVar=777

def outFunc():
    
    def inFunc():
        memVar = 'inin'
        print(memVar)
    memVar = 'outout'
    inFunc()
    print(memVar)
    
outFunc()
print(memVar)