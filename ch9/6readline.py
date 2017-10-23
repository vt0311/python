'''
Created on 2017. 10. 23.

@author: acorn
'''

with open('test2.txt', 'r') as file6:

    str = file6.readline()
    while str != '':
        print(str)
        str = file6.readline()
