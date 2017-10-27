'''
Created on 2017. 10. 27.

@author: acorn
'''
def func4(mylist) :
    imsi = []
    for item in range(len(mylist)-1, -1, -1) :
        imsi.append(mylist[item])
    
    return imsi