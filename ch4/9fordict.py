'''
Created on 2017. 10. 19.

@author: acorn
'''
dict1 = {'Jane' : 'SU' , 'john':'MIT', 'Jake':'NYU', 'Jack':'CU' }

for key in dict1.keys():
    print(key)
    
print('=================================')
 
 
for val in dict1.values():
    print(val)    
    
    
print('=================================')


for it1, it2 in dict1.items():
    print(it1, it2)    
    
print('=================================')



for its in dict1.items():
    print(type(its))
    print(its[0], its[1])
    

print('=================================')

for ditem in dict1.items():
    print('{}:{}'.format(*ditem))    
    