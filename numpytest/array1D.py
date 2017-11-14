'''
Created on 2017. 11. 14.
카페 189번
@author: acorn
'''
import  numpy as np

arr = np.array([1, 2, 3])

print('\n 배열의 타입 확인:', type(arr))


print(arr[0], arr[1], arr[2])
print()

print('\n shape는 각 차원의 크기를 알려주는 정수들이 모인 튜플이다.')
print('배열 차원의 크기:', arr.shape)
print()

arr[0] = 5
print('배열 요소 출력 : ', arr)
print()

print(arr.dtype)
