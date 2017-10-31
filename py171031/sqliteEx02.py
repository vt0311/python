'''
Created on 2017. 10. 31.

@author: acorn
'''

import sqlite3
import pandas as pd
from datetime import date
from fileinput import filename


# getAllInfo : 반복문을 이용하여 해당 커서의 정보를 모두 출력
def getAllInfo(mycursor): 
    for onetuple in mycursor :
        print('아이디: ' + onetuple[0], end='') 
        print(', 과목: ' + onetuple[1], end='') 
        print(', 점수: ' + str(onetuple[2]), end='')
        print()
        
conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()

# Create table
try :
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
    
mycursor.execute('''CREATE TABLE sungjuk
        (id text, subject text, jumsu integer)''')

# filename = 'getjumsu.csv'
# myframe = pd.read_csv(filename)
# rowsize = myframe.index.size
# arr2d = print( myframe.values)
# print(myframe)
# print(myframe.index)
# 
# for idx in myframe.index:
#     print( myframe[ idx ])
#     print( type(idx))

mycursor.execute('insert into sungjuk values ("lee", "java", 10)')
mycursor.execute('insert into sungjuk values ("lee", "html", 10)')
mycursor.execute('insert into sungjuk values ("lee", "python", 10)')

conn.commit()

# 다량의 데이터 한꺼번에 추가하기
datamylist = [ ('jo', 'java', 40), ('jo', 'html', 50), ('jo', 'python', 60), \
               ('ko', 'java', 70), ('ko', 'html', 80), ('ko', 'python', 90), ]

mycursor.executemany('insert into sungjuk values(?,?,?)', datamylist)

conn.commit()


mycursor.execute("SELECT * FROM sungjuk")

print('------------------------------')
getAllInfo(mycursor) # 함수 형태로 구현

#print(mycursor.fetchall())


print('-------------------------')

for row in mycursor.execute('SELECT * FROM sungjuk ORDER BY id, subject'):
    print(row)
    
  
conn.close()
print()
print('작업완료')
    
    







 