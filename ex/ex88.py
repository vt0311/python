'''
Created on 2017. 10. 26.

@author: acorn
'''

marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks :
    number += 1 
    
    if mark >= 60 :
        print('{}번째 응시자 {}점 합격'.format(number, mark))
    else :
        print('{}번째 응시자 {}점 불합격'.format(number,mark))
        
        
