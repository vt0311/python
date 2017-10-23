'''
Created on 2017. 10. 23.

@author: acorn
'''
import sqlite3

conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

#cursor.execute("CREATE TABLE board(title text, writer text, contents text, reg_date text) ")
cursor.execute("CREATE TABLE diary(title text, weather text, contents text, reg_date text) ")
cursor.close()

conn.close()

