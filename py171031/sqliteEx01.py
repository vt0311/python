'''
Created on 2017. 10. 31.

@author: acorn
'''
import sqlite3
import pandas as pd  

dbname = 'sqlitedb.db'
conn = sqlite3.connect(dbname)

mycursor = conn.cursor()

try:
     mycursor.execute('drop table students')
except sqlite3.OperationalError:
     print('테이블이 존재하지 않습니다.')
    

# statement = '''create table students 
#                 (id text primary key, name text, birth text)'''
#     
mycursor.execute('''create table students (id text primary key, name text, birth text)''')

statement = ' insert into students(id, name, birth)'
statement += ' values( "lee", "이승기", "1988/12/25")'
mycursor.execute( statement)


statement = ' insert into students(id, name, birth)'
statement += ' values( "kang", "강감찬", "1911/11/15")'
mycursor.execute( statement)

statement = ' insert into students(id, name, birth)'
statement += ' values( "kang2", "강감찬2", "1911/11/15")'
mycursor.execute( statement)
    
datamylist = [('jo', '조권', '1985/03/01'), ('ko', '고아라', '1985/11/01')]    
mycursor.executemany( 'insert into students(id, name, birth) values ( ? , ?, ? )', datamylist )
    
conn.commit()

findid = 'ko'

mycursor.execute("select * from students where id = '%s'" % findid)

result = mycursor.fetchone()

print( '아이디 : ' + result[0], end = '' )
print( ', 이름 : ' + result[1], end = '' )
print( ', 생일 : ' + result[2], end = '' )
print()
print()

mycursor.close()
conn.close()

print('작업 종료')
