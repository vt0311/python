'''
Created on 2017. 10. 31.
#1412 join 테스트
@author: acorn
'''
import sqlite3
import pandas as pd  
from datetime import date

dbname = 'sqlitedb.db'
conn = sqlite3.connect(dbname)

mycursor = conn.cursor()

# try:
#      mycursor.execute('drop table students')
# except sqlite3.OperationalError:
#      print('테이블이 존재하지 않습니다.')
#     

# statement = '''create table students 
#                 (id text primary key, name text, birth text)'''
#     
# mycursor.execute('''create table students (id text primary key, name text, birth text)''')
# 
# statement = ' insert into students(id, name, birth)'
# statement += ' values( "lee", "이승기", "1988/12/25")'
# mycursor.execute( statement)
# 
# 
# statement = ' insert into students(id, name, birth)'
# statement += ' values( "kang", "강감찬", "1911/11/15")'
# mycursor.execute( statement)
# 
# statement = ' insert into students(id, name, birth)'
# statement += ' values( "kang2", "강감찬2", "1911/11/15")'
# mycursor.execute( statement)
#     
# datamylist = [('jo', '조권', '1985/03/01'), ('ko', '고아라', '1985/11/01')]    
# mycursor.executemany( 'insert into students(id, name, birth) values ( ? , ?, ? )', datamylist )
#     
# conn.commit()
# 
# findid = 'ko'

#mycursor.execute("select * from students where id = '%s'" % findid)

#result = mycursor.fetchone()

# print( '아이디 : ' + result[0], end = '' )
# print( ', 이름 : ' + result[1], end = '' )
# print( ', 생일 : ' + result[2], end = '' )
# print()
# print()

# 조인 사용해보기
sql = ' select st.id, st.name, st.birth, '
sql += ' sg.subject, sg.jumsu'
sql += ' from students st '
sql += ' join sungjuk sg '
sql += ' on st.id = sg.id '

mycursor.execute( sql )

print('결과')
result = mycursor.fetchall()
print(result)
print()

print('타입 확인')
print( type(result) )
print()

for row in mycursor.execute(sql):
    print(row)
print()
#mycursor.close()
conn.close()
print()
print('작업 종료')
