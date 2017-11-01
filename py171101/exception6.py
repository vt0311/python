'''
Created on 2017. 11. 01.

@author: acorn
'''

def soshiCheck(finddata):
    soshi = ["서현", "수영", "써니", "유리", "윤아", "제시카", "태연", "티파니", "효연" ]
    isMember = False
    
    for member in soshi :
        if member == finddata:
            isMember = True
            break
        
    if isMember == True:
        print('소시 멤버 맞아요')
    else:
        msg = '소시 멤버가 아니에요'
        raise Exception(msg)
    
name = '제시카'
#name = '윤종신'

try:
   soshiCheck(name)

except Exception as err :
    print("예외 발생 : {0}".format(err))


