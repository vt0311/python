'''
Created on 2017. 11. 14.
카페 25번
@author: acorn
'''
import  numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr)

print()


mylist = []

for item in arr : 
    mylist.append(item * 2)
    
    
print(mylist)
print()

print( 2 * arr)
print()

print(2 * mylist)
print()

a = np.array([1,2,3])
b = np.array([10,20,30])

print(2*a + b)
print()

print(np.exp(a))
print()

print(np.log(b))
print()

print(np.sin(a))
print()

mylist = [0, -3, np.nan, -6]
print(np.abs(mylist))
print()