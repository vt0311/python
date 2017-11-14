'''
Created on 2017. 11. 14.

@author: acorn
'''
import numpy as np

arrX = np.array([[1,2],[3,4]])
arrY = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11,12])

# v와 w의 요소들간의 곱셈 결과를 모두 더하기
print(v.dot(w))
print()

print(np.dot(v, w))
print()

print(arrX.dot(v))
print(np.dot(arrX, v))
print()

print(arrX.dot(arrY))
print(np.dot(arrX, arrY))
print()