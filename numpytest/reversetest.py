'''
Created on 2017. 11. 14.

@author: acorn
'''
import numpy as np

arrA = np.array([[4,5], [3,4]])

print(arrA)

print()


invA = np.linalg.inv(arrA)
print(invA)
print()

result = np.dot(arrA, invA)
print(result)
print()

arrB = np.array([[4,2],[8,4]])
print(arrB)
print()

D = arrB[0,0] * arrB[1,1] - arrB[0, 1] * arrB[1,0]

if D == 0 :
    print('역행렬이 존재하지 않습니다.')
    
else :
    invB = np.linalg.inv(arrB)
    print(invB)
    print()
    
    result = np.dot(arrB, invB)
    print(result)
    print()    

