'''
Created on 2017. 10. 19.

@author: acorn
'''

def funcVar(in1, in2):
    print('{}을(를) {}합니다.'.format(in1, in2))
    

    
funcVar('죽음의 스누피', '거부')

tuple1 = ('여러분',  '환영')

funcVar(*tuple1)    

print('=============================')
aaaVar = funcVar

aaaVar(*tuple1)

print('=============================')

list1 = [aaaVar]

list1[0](*tuple1)

funcVar('죽음의 스누피', '거부')
