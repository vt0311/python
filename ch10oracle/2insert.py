'''
Created on 2017. 10. 23.

@author: acorn
'''

import sqlite3


conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

cursor.execute("insert into diary values('2nd','ro2','hi2','20171023')")

conn.commit()

cursor.close()

conn.close()




