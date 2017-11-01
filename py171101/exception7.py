'''
Created on 2017. 11. 01.

@author: acorn
'''

class LessThan5Exception(Exception):
    def __init__(self, arg):
        # Exception 클래스에 예외 message를 넘긴다.
        super().__init__('{}는 5보다 작은 수입니다.'.format(arg))

su = input('5이상의 수를 입력하세요:')

try :
    su = int (su)
    if (su < 5 ):
        raise LessThan5Exception(su)
    else :
        print('잘 하셨습니다.')
        
except LessThan5Exception as err :
    # 넘겨준 예외 message 를 출력한다.
    print("예외 발생 : %s" % err )
    
except ValueError as err :
    print('숫자 넣어주세요 : %s ' % err)
    


