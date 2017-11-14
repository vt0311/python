'''
Created on 2017. 11. 14.
카페 30번
@author: acorn
'''
import  numpy as np


arrX = np.array([[1,2], [3,4]], dtype=np.float64)
arrY = np.array([[5,6], [7,8]], dtype=np.float64)

print(arrX + arrY)
print(np.add(arrX, arrY))


print(arrX - arrY)
print(np.subtract(arrX, arrY))


print(arrX * arrY)
print(np.multiply(arrX, arrY))


print(arrX / arrY)
print(np.divide(arrX, arrY))

print(np.sqrt(arrX))