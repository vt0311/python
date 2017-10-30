'''
Created on 2017. 10. 30.

@author: acorn
'''
import re

mystr = 'abcd 1234 abAB'

regex = '[a-d]+'

pattern = re.compile(regex)

# findall 
mylist = pattern.findall(mystr)

print(mylist)

myiter = pattern.finditer(mystr)
for abcd in myiter :
    print( abcd)