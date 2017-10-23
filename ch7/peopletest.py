'''
Created on 2017. 10. 20.

@author: acorn
'''

from ch7.student import Student
from ch7.teacher import Teacher

stu = Student()
stu2 = Student()
stu.name = 'lee'
stu2.name = 'song'

print(stu.name)
print(stu2.name)

stu.talk()

tea = Teacher()
tea.humor()
tea.talk()
 





