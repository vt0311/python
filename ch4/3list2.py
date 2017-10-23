'''
Created on 2017. 10. 19.

@author: acorn
'''

list1 = {1,2,3,4,5,6,7}

list2 = list1

print(list2)

list2[0] = 777


print('list2', list2)

print('list1', list1)

list3 = list1.copy()

list3[1] = 999

print('list3', list3)
print('list2', list2)

print('list1', list1)