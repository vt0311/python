'''
Created on 2017. 10. 19.

@author: acorn
'''

inname = input('이름을 입력하세요:')

''' not in : 입력한 그 값이 없는 동안 계속 루프를 돈다 '''
while inname not in ['jane', 'jake', 'jack', 'john']:
    
    inname = input('이름을 입력하세요:')

print('end of while')

