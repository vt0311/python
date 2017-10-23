'''
Created on 2017. 10. 20.

@author: acorn
'''

class Parent7:
    def chullyuk(self):
        print('Parent7.chullyuk')
        
class Child5(Parent7):
    def chullyuk(self):
        super().chullyuk()
        print('Child5.chullyuk')
        
c5 = Child5()

c5.chullyuk()

