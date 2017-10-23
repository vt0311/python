'''
Created on 2017. 10. 20.

@author: acorn
'''
from ch7.people import People

class Student(People):
    
    scard=''
    tel=''
    grade=''
    clsno=''
    
        
    def talk(self):
        print('학생이 말을 한다')