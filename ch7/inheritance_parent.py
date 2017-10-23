'''
Created on 2017. 10. 20.

@author: acorn
'''

''' 상속은 부모클래스의 멤버 변수와 멤버 메소드를 
자식 클래스에서 사용하는 것'''

class Parent1:
    name = 'Parent1'
    def chullyuk(self):
        print('Parent1.chullyuk')
        
class Parent2:
    name = 'Parent2'
    
class Child (Parent1):
    age = ''
    
c1 = Child()

print(c1.name)    

c1.chullyuk()