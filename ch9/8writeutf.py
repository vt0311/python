'''
Created on 2017. 10. 23.

@author: acorn
'''

list1 = ['안녕. ', '반가워. ', '어떻게 지냈니?']

with open('test4.txt', 'w', encoding = 'utf-8') as file8:
    for itm in list1:
        file8.write(itm)