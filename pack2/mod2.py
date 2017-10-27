'''
Created on 2017. 10. 27.

@author: acorn
'''

def func1(num, mylist) :
    cnt = 0;
    for item in range(len(mylist)):
        if num >= mylist[item]:
            cnt = cnt + 1
            #cnt++
    return cnt

  


