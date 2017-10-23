'''
Created on 2017. 10. 19.

@author: acorn
'''

''' 순서 없고 '''
dict1 = {'john':25, 'jane':26}


print(dict1)

print(type(dict1))
print(dict1['john'])
dict1['john'] = 27
print(dict1)
print("length : ", len(dict1))

print(())
#v8, v9 = dict1
'''
print(v8)
print(dict1(v8))

print(v9)
print(dict1(v9))
'''


dict2 = {'john':31, 'jack': 32} 

dict1.update(dict2)
print(dict1)

dict1.pop('jack')
print(dict1)

print(dict1.keys())
print(type(dict1.keys()))
print(dict1.values())
print(type) 
print()
