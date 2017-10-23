'''
Created on 2017. 10. 19.

@author: acorn
'''

'''
for i in range(2,10):
    for k in range(1,10):
        if i % 2 == 0:
            break;
        print('{} * {} = {}'.format(i, k, i*k)
    print()
    
'''

for i in range(2,10):
    for k in range(1,10):
        if i % 2 == 0:
            continue
        print('{} * {} = {}'.format(i, k, i*k))
    print()