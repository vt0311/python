'''
Created on 2017. 10. 23.

@author: acorn
'''
import sqlite3

conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

cursor.execute('delete from board')

conn.commit()

cursor.close()

conn.close()