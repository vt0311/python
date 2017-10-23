'''
Created on 2017. 10. 19.

@author: acorn
'''
for i in range(1,11):
    for k in range(10, 0, -1):
        print(' ', end='')
        if i == k:
            break
    for z in range(1,11): 
        print('★', end = '')
        if i == z:
            break  
        
    print()