'''
Created on 2017. 10. 23.

@author: acorn
'''
import sqlite3


conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

cursor.execute("update board set writer = 'hah' where title ='1st'")

conn.commit()

cursor.close()

conn.close()