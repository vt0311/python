'''
Created on 2017. 10. 19.

@author: acorn
'''

list1 = [1, 2, 3, 4, 5]

for val in list1 :
    print(val)
    
list2 = ['hi', 'hello', 'good']     
    
for val in list2:
    print(val)
 
 
for val in enumerate(list2):
     print(type(val))
     print('{}번지 : 값{}'.format(val[0], val[1]))   
    
    