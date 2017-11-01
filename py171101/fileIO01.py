'''
Created on 2017. 11. 1.
파일 입출력 1
@author: acorn
'''

# 파일을 쓰기 모드로 오픈한다.
myfile1 = open('newFile.txt', 'w', encoding='utf-8')

for i in range(1, 11):
    data = '%d번째 줄입니다\n' % i
    myfile1.write(data) # 파일에 기록한다.
    
myfile1.close() # 파일 닫기 작업

# 여러개의 파일 만들기
for i in range(1, 11):
    myfile = open('somefile' + str(i) + '.txt', 'w', encoding='utf-8' )
    data = '%d 번째 내용\n' % i
    myfile.write(data)
    myfile.close()

# 파일 쓰기 모드에서 a는 추가 모드 이다.    
myfile3 = open('newFile.txt', 'a', encoding='utf-8')    

for i in range(11, 21):
    data = '%d번째 줄입니다.\n' % i 
    myfile3.write(data)
    
#myfile3.close()

for j in range(31, 40, 2):
    data = '%d번째 줄 입니다.\n' % j
    myfile3.write(data)

myfile3.close()


myfile4 = open('abc.txt', 'a', encoding='utf-8')

for i in range(1, 10):
    for j in range(1, 10):
        
       #data2 = '%d'+'*'+ '%d' + '='+'%d \n' % (i, j , i*j )
       #data2 = '{} * {} = {} \n'.format(i, j , i*j )
        data2 = '%d * %d = %d \n' % (i, j , i*j )
        myfile4.write(data2)
    
myfile4.close()
    

# with 구문 사용하기
# with 구문을 벗어나는 순간 객체가 자동으로 close() 된다.
# print 함수의 매개변수로 file에 파일객체를 대입하면
# 콘솔에 출력하지 않고 파일에 출력할 수 있다.

with open('test.txt', 'w', encoding='utf-8') as myfile :
    print('하하하', file = myfile)
    print('호호호', file = myfile)
    
with open('test.txt', 'r', encoding='utf-8') as file :
    print( file.read())
        


print('aa', 'bb')
print('aa', 'bb')
print('aa', 'bb', sep='')
print('aa', 'bb', 'cc', end='')
print('dd')


print('작업 완료')