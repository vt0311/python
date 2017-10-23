'''
Created on 2017. 10. 19.

@author: acorn
'''
list1 = [1,2,3,4,5]
print(list1)
print('type:', type(list1))

'''index'''
print('index 0:', list1[0])
print(list1[0])
#list[0] = 7
print(list1)

'''length'''
print('length:', len(list1))

#print(list1[0], )
list1.append(6)
print(list1)

list2 = list1  + [5, 4, 3 ,2 ,1 ]
print(list2)

list1.extend(list2)
print(list1)


print(6 in list1)

print(list1.index(6))

print(list1.count(6))



list1.sort()
print(list1)

list1.reverse()
print(list1)


