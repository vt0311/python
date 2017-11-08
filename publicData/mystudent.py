'''
Created on 2017. 11. 8.

@author: acorn
'''
from xml.etree.ElementTree import parse
from pandas import DataFrame

tree = parse('mystudent.xml')
myroot = tree.getroot() # 최상위 엘리먼트 취득

allstudents = myroot.findall('student')

#print( allstudents )
print()

totallist = []

for onestudent in allstudents:
    childs = onestudent.getchildren()
    sublist = [] 
    for onedata in childs:
        mydata = onedata.text.replace(',', '')
        mydata = mydata.replace('"', '')

        sublist.append( mydata )
        
        
    total = float(sublist[1])+ float(sublist[2]) + float(sublist[3])
    mean = float(total / 3.0 )
    
    sublist.append(str(mean))
    sublist.append(str(total))
    
        
#     for onedata in [0,5]:   
#         sublist.append( mydata )
    
    totallist.append(sublist)
    
mycolumn = ['이름', '국어', '영어', '수학', '평균', '총점']

myframe = DataFrame(totallist, columns = mycolumn)

# 필요한 열만 재색인한다.
#myframe = myframe.reindex( columns = mycolumn )

# 컬럼 이름을 영문이름으로 맵핑 시킨다.
#myframe = myframe.rename( columns = col_mapping )

print()
print(myframe)
print()

import sqlite3
import pandas as pd

conn = sqlite3.connect('inchon.db')

# cursor(커서) : 실제 db에 접속해서 무엇인가를 요청하는 객체
mycursor = conn.cursor()

try:
    mycursor.execute("drop table students")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''CREATE TABLE students
             (name text primary key, kor text, eng text, math text, mean text, total text)''')


for onedata in range(len(myframe)):
    imsi = myframe.ix[onedata]
    name = imsi['이름']
    kor = imsi['국어']
    eng = imsi['영어']
    math = imsi['수학']
    #mean = (int(kor) + int(eng) + int(math))/3
    mean = imsi['평균']
    #total = int(kor) + int(eng) + int(math)
    total = imsi['총점']
    sql = "insert into students values('" + name + "', '" +  kor + "', '" + eng + "', '" + math + "', '" + mean + "', '" + total + "')"
    # print( sql )
    mycursor.execute( sql )

conn.commit()



saved_folder = 'c:/work/'
result = [] # 비어 있는 리스트


sql = "select * from students"
for row in mycursor.execute( sql ):
    # print (type(row)) # <class 'tuple'>
    print (row)
print()


std_table = pd.DataFrame(\
                         result, \
                         columns=('name', 'kor', 'eng', 'math', 'mean', 'total'))

std_table.to_csv(saved_folder + "std_table.csv", encoding="cp949", \
                 mode='w', \
                 index=True)


import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')



mycursor.close()
conn.close()
print()
print('작업 완료')
