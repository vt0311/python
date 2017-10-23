'''
Created on 2017. 10. 20.

@author: acorn
'''

class StrTest:
    memStr = 'str test'
    def __str__(self):
        print('StrTest:', self.memStr)
        return 'StrTest:'+self.memStr
   
 
stest = StrTest()
print(stest)    
    
    #\def __str__(self) :
         

