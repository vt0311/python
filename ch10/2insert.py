'''
Created on 2017. 10. 23.

@author: acorn
'''

import sqlite3


conn = sqlite3.connect('pytest.db')

cursor = conn.cursor()

#cursor.execute("insert into board values('1st','ro','hi','20171023')")
#cursor.execute("insert into board values('2nd','ro2','hi2','20171023')")
cursor.execute("insert into diary values('2nd','ro2','hi2','20171023')")

conn.commit()

cursor.close()

conn.close()




