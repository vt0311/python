'''
Created on 2017. 10. 27.

@author: acorn
'''
sum = lambda a, b : a + b

print( sum(3,4))

#리스트 내에 lambda a, b : a + b, lambda a, b : a * b]
list1 = [lambda a, b : a + b, lambda a, b : a* b]
print(list1)

print(list1[0](5,4))
print(list1[1](5,4))