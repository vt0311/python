'''
Created on 2017. 10. 23.

@author: acorn
'''

file1 = open('test1.txt', 'w')
'''open함수 - 파일 없으면 만들고, 있으면 연결하고 '''

file1.write('test1 test - hello')

file1.close()
'''반드시 close() 한다'''
