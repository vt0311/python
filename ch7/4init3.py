'''
Created on 2017. 10. 20.
파이썬에서 생성자는 init 이다.
@author: acorn
'''

'''예제1'''
class CTest3:
    
    memStr='before'
    
ctest3 = CTest3()
    
print('ctest3 :', ctest3.memStr)

 
class ConTest:
    memStr = 'before'
    def __init__(self, str):
        self.memStr = str
        
print('==================================================')
    
'''예제3 기본 생성자도 잘 돌아간다'''   
        
class ContructorTest3:
    
    memStr = 'before'
    
    def __init__(self, inData):
        self.memStr = inData
    
        print('생성자:' , self.memStr)
        
ctest = ContructorTest3('after')
print(ctest.memStr)
    
