'''
Created on 2017. 10. 20.

@author: acorn
'''

class IDException(Exception):
    def __init__(self):
        super().__init__('ID NOT Found Exception')
        
def idCHK(inID):
    saveID = 'abcdefg'        

    if(inID != saveID):
        raise IDException 

inID = input('ID 입력: ')

#saveID = 'abcdefg'
try:
    idCHK(inID)
    
except IDException as ex:
    print('ID를 찾을 수 없습니다.', ex)
    
else:     
    print('환영합니다.')
    
finally:
    print('login process complete!!')
