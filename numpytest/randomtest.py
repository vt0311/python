'''
Created on 2017. 11. 14.

@author: acorn
'''
import numpy as np

result = np.random.random((2,2))
print(result)
print()

result = np.random.randint(0, 5, size=10)
print(result)
print()

length = 5
result = np.random.permutation(length)
print(result)
print()

result = np.random.randint(5)
#result = np.random.randint(45) + 1
print(result)
print()
