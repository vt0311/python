'''
Created on 2017. 10. 20.

@author: acorn
'''

class TestClass:

    memInt = 777
    
    def testMethod(self, memInt):
        self.memInt = memInt
    

test = TestClass()
print(test.memInt)
test.testMethod(54321)
print(test.memInt)