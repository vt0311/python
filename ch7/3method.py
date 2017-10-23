'''
Created on 2017. 10. 20.

@author: acorn
'''

class TestClass2 :
    
    memmem = 777
    
    def testMethod2(self, memmem):
        print('memmem:',memmem)  # 54321 출력
        print('self.memmem:',self.memmem)  # 777 출력 
        

test2 = TestClass2()

test2.testMethod2(54321)    
        