'''
Created on 2017. 10. 20.

@author: acorn
'''


class Parent4:
    def __int__(self):
        print('parent4.init')
        
class Parent5:
    def __init__(self):
        print('parent5.init')
        
class Child4(Parent4, Parent5):
    def __init__(self):
        super().__init__()
        print('Child3.init')


c3 = Child4()
#c3.name        