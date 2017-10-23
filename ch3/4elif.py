'''
Created on 2017. 10. 19.

@author: acorn
'''

varA = int(input('시험점수입력:'))

if varA > 100:
    print('사기 금지')
    
elif varA >= 90:
    print('A학점')

elif varA >= 80:
    print('B학점')
    
elif varA >= 70:
    print('C학점')
    
elif varA >= 60:
    print('D학점')
    
else :
    print('재시험')        