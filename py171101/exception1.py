'''
Created on 2017. 11. 01.

0으로 나누기(예외 처리)

@author: acorn
'''

x = 4
y = 0

list1 = [1, 2, 3]

try:
    print(list1[4])
    z = x / y
    print('하하하')
     
except ZeroDivisionError  as err:
    pass # pass는 오류를 발생시키지 않고 그냥 통과한다.
    print(err) #
    print('0으로 나눌수 없습니다.')

except IndexError as err :
    print(err)
    print('인덱스 오류.')
    
else : # except 구문에 상반되는 개념으로 만듬
    print('예외가 없으면 실행이 된다.')
    
finally:
    print('예외 발생 여부와 상관없이 무조건 실행')


