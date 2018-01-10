'''
Created on 2017. 10. 23.

@author: acorn
'''
import sqlite3

conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

#cursor.execute('select * from board')
cursor.execute('select * from diary')
#cursor.execute('select title from diary')

rows = cursor.fetchall()

for row in rows:
    print(row) 

print(rows)

cursor.close()

conn.close()