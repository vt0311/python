'''
Created on 2017. 10. 20.

@author: acorn
'''


class Parent2:
    names='Parent2'
    def chullyuk(self):
        print('Parent2.chullyuk')
        
class Parent3:
    names='Parent3'
    def chullyuk(self):
        print('Parent3.chullyuk')
class Child2(Parent2, Parent3):
    age=''
    
c2 = Child2()
print(c2.name)        
c2.chullyuk()