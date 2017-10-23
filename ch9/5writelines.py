'''
Created on 2017. 10. 23.

@author: acorn
'''

list2 = ['hi', 'hello', 'good']
list3 = [1,2,3]

with open('test3.txt', 'w') as file5:
    file5.writelines(list2)
    #file5.writelines(list3) # 문자열만 됨