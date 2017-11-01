'''
Created on 2017. 11. 01.

파일 미존재(예외 처리)

@author: acorn
'''



try:
    
    print('파일을 읽기 모드로 오픈한다.')
    myfile1 = open('asdf.txt', 'r')

    print('\n# readline() 함수는 1줄은 읽어온다.')
    line = myfile1.readline()
    print('읽어온 데이터 : ', line)
    
    print('\n# 모든 라인을 읽어 들이고, 출력한다.')
    
    while True:
        line = myfile1.readline()
        if not line :
            break
        print(line)
    
    myfile1.close()
    
except FileNotFoundError as err:
    print('찾으시는 파일이 없습니다.')    
    
else : 
    print('예외가 없으면 실행이 된다.')
    
#finally:
#    print('예외 발생 여부와 상관없이 무조건 실행')