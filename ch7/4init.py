'''
Created on 2017. 10. 20.
파이썬에서 생성자는 init 이다.
@author: acorn
'''

'''예제1'''
class CTest:
    
    memStr='before'
    
ctest1 = CTest()
    
print('ctest1 :', ctest1.memStr)
 
class ConTest:
    memStr = 'before'
    def __init__(self, str):
        self.memStr = str
    
'''예제3'''   
class ContructorTest:
    
    memStr = 'before'
    
    def __init__(self, str):
    
        self.memStr = str
        
ctest = ContructorTest('after')
print(ctest.memStr)
    
