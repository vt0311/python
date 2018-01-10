'''
Created on 2017. 10. 23.

@author: acorn
'''

'''
diary
reg_date text
weather
title
contents


조회 입력 수정 삭제

'''
import sqlite3
from ch10.diary import DiaryVO


def insFunc(*instr):
    sql="insert into diary values('{}','{}','{}','{}'}".format(*instr)


conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()


#dList = []

while True:
    print("======== my diary =======")
    menuInt = int(input('선택 (0:종료, 1:입력, 2:출력, 3:삭제) : '))

    if(menuInt == 0):
        break
    
    elif(menuInt == 1):
        #dr = DiaryVO()
       
        title = input('제목을 입력:')
        weather = input('날씨를 입력:')
        contents = input('내용을 입력:')
        reg_date = input('날짜를 입력:')
        
    #    dList.append(dr)
        
        #sql = "insert into diary values(%s, %s, %s, %s)"
        #title text, weather text, contents text, reg_date text
        #cursor.execute(sql, (title, weather, contents, reg_date))
        cursor.execute("insert into diary values('"+title+"', '"+weather+"', '"+contents+"', '"+reg_date+"')")
         #cursor.execute("insert into diary (title, weather, contents, reg_date) values (title1, weather1, contents1, reg_date1)")
        conn.commit()
        #cursor.close()

        #conn.close()
    elif(menuInt == 2):
        
        cursor.execute('select * from diary')

        rows = cursor.fetchall()    
        
        for row in rows:
            print(row) 

            print(rows)

        '''
        for i in range(len(dList)):
            print(dList[i].reg_date)
            print(dList[i].weather)
            print(dList[i].title)
            print(dList[i].contents)
            print(dList[i].reg_date)
            print('======================')
       '''
        #cursor.close()

        #conn.close()  
    elif(menuInt == 3):
        instr1 = input("삭제할 일기의 날짜 : ") 
        
            
        conn.commit()    
          
    else:    
        print('wrong input!!! try again!!!')    
        
        
cursor.close()

conn.close() 
