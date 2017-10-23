'''
Created on 2017. 10. 19.

@author: acorn
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list1[0:10])


print(list1[:5])


print(list1[0:])


print(list1[11:17])

print(list1[3:17:2])

del(list1[1:5])

print(list1)

list1[0:1] = [9, 8, 7]

print(list1)


list1[0:2] = [0,1,2,3,4,5]

print(list1)