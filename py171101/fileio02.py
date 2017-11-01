'''
Created on 2017. 11. 1.

@author: acorn
'''
print('파일을 읽기 모드로 오픈한다.')

myfile1 = open('newFile.txt', 'r', encoding='utf-8')

print('n# readline() 함수는 1줄은 읽어 온다.')

line = myfile1.readline()

print('읽어온 데이터 : ', line)

print('\n# 모든 라인을 읽어 들이고, 출력한다.')

while True :
    line = myfile1.readline()
    if not line :
        break
    print( line )
    
myfile1.close()

print('----------------------')

myfile2 = open('newFile.txt', 'r', encoding='utf-8')

print('\n# readline() 함수는 파일의 모든 라인을 읽어서 리스트로 만들어 준다.')

linelists = myfile2.readlines()

for oneline in linelists:
    print(oneline)
    
myfile2.close()
print('----------------------')

myfile3 = open('newFile.txt', 'r', encoding='utf-8')

print('\n# read() 함수는 파일의 내용 전체를 문자열로 반환한다.')

allcontents = myfile3.read()

print(allcontents)

myfile3.close()

print('작업 완료')