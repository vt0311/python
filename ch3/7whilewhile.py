'''
Created on 2017. 10. 19.

@author: acorn
'''

initV1 = 2

while initV1 < 10 :
    
    initV2 = 1
    
    while initV2 < 10:
        print('{} * {} = {}'.format(initV1, initV2, initV1* initV2))
        initV2 = initV2 + 1
    print()
    initV1 = initV1 + 1
print('end of while 구구단')   