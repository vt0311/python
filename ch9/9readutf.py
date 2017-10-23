'''
Created on 2017. 10. 23.

@author: acorn
'''

with open('test4.txt', 'r', encoding='utf-8') as file9:
    str= file9.readline()
    while str != '':
        print(str, end='')
        str = file9.readline()