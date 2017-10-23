'''
Created on 2017. 10. 23.

@author: acorn
'''

list1 = ['hi', 'hello', 'good']

with open('test2.txt', 'w') as file4:
    for item in list1:
        file4.write(item+'\n')