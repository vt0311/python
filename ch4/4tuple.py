
'''
Created on 2017. 10. 19.

@author: acorn
'''



tuple1 = (1,2,3,4,5)

print(tuple1)

print(type(tuple1))

print('index 2 : ', tuple1[2])

print('length : ', len(tuple1))

#tuple1[0] = 7 #error

tuple1 = tuple1 + (6,7)

print(tuple1)

print('====================================')

tuple1 = tuple1 + ('hi', 'hello')

print(tuple1)

print('================================')


list1 = [9, 8, 7, 6, 5, 4]

tuple2 = tuple(list1)

print(tuple2)
print('index :', tuple2.index(7))

print('count :', tuple2.count(4) )
