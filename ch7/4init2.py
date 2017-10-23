'''
Created on 2017. 10. 20.
파이썬에서 생성자는 init 이다.
@author: acorn
'''

'''예제1'''
class CTest2:
    
    memStr='before'
    
ctest2 = CTest2()
    
print('ctest1 :', ctest2.memStr)
 
class ConTest:
    memStr = 'before'
    def __init__(self, str):
        self.memStr = str
    
'''예제3 기본 생성자도 잘 돌아간다'''   
        
class ContructorTest2:
    
    memStr = 'before'
    
    def __init__(self):
    
        print('기본 생성자 돌았음')
        
ctest = ContructorTest2('after')
print(ctest.memStr)
    
