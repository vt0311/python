'''
Created on 2017. 11. 1.

@author: acorn
'''

print('\n 파일을 읽기 모드로 오픈한다')

myfile3 = open('jumsu.txt', 'r')

print('\n readline() 함수는 모든 라인을 읽어서 리스트로 만들어 준다')
linelists = myfile3.readlines()
print('읽어온 데이터:', linelists)



myfile3.close()

print('--------------------------------')

myfile4 = open('result.txt', 'w', encoding='utf8')

for item in linelists :
    # mylist : 콤마로 분리된 list 자료형
    mylist = item.split(',')
    name = mylist[0]
    kor = float(mylist[1])
    eng = float(mylist[2]) 
    math = float(mylist[3])
    gender0 = mylist[4]
    
    total = kor + eng + math
    average = total / 3.0
    
    if gender0 == 'M' :
        gender = '남자'
        
    else :
        gender = '여자'
        
    # %10.2f : 10은 넉넉한 임의의 숫자, .2은 소수점 2자리까지 표시
    avg = ('%10.2f' % average)
    avg = avg.strip()
    
    imsi = name + '/' + gender + '/' + str(total) + '/' + avg
    
    myfile4.write(imsi + '\n')
    
myfile4.close()
print('작업 종료')    