'''
Created on 2017. 10. 19.

@author: acorn
'''

''' 구구단 '''

#initv1 = 2

for initv1 in range(2, 10 ) :
    print("{}단".format(initv1))

    #initv2 = 1
    
    for initv2 in range(1, 10) :
    
        print('{} * {} = {}'.format(initv1, initv2, initv1 * initv2 ))
    print()
print('구구단 종료')    

