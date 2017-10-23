'''
Created on 2017. 10. 19.

@author: acorn
'''

while True :
    menu = input('0:종료, 1:입력, 2:출력 : ')
    if menu == '0':
        break;
    elif menu == '1':
        print('입력이 나오는 로직이 나오면 됨')
    elif menu == '2':
        print('출력을 수행하는 로직이 나오면 됨')
    else:
        print('잘못 입력함')
print('끝')            
            