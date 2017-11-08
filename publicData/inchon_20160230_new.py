from xml.etree.ElementTree import parse
from pandas import DataFrame

tree = parse('inchon_20160229.xml')
myroot = tree.getroot() # 최상위 엘리먼트 취들

# print( type(myroot))

# <Row>라는 엘리먼트에 업체 1군데의 정보가 들어 있다.
# allstores : 모든 업소에 대한 정보
allstores = myroot.findall('Row')
print( 'findall는 일치하는 모든 태그를 리스트로 반환한다.' )
#print( allstores )
print( len(allstores) )
print( type(allstores) )
print()

totallist = [] #모범 음식점의 정보들을 저장할 리스트
for onestore in allstores:
    childs = onestore.getchildren()
    sublist = [] # 1개의 음식점 정보
    for onedata in childs:
        # 콤마와 쌍따옴표는 빈 문자열로 처리하도록 한다.
        mydata = onedata.text.replace(',', '')
        #mydata = mydata.text.replace('"', '')
        mydata = mydata.replace('"', '')
        sublist.append( mydata )
        #print('-------------------')
    totallist.append(sublist)
    #print('-------------------')
    
print( totallist)

print('-------------------------------------------------')
mycolumn = ['업소명', '소재지 도로명', '전화 번호', '주된 음식']
# myframe은 모범 음식점 정보를 담고 있는 DataFrame이다.
myframe = DataFrame(totallist, columns=mycolumn)
# print( type(myframe) ) # <class 'pandas.core.frame.DataFrame'>
print()
print(myframe)
print()

# myframe.to_csv('datainchon.csv', encoding='EUC-KR')
# print( '작업 완료' )

# sqlite3를 사용하기 위하여 임포트
import sqlite3
import pandas as pd

conn = sqlite3.connect('inchon.db')

# cursor(커서) : 실제 db에 접속해서 무엇인가를 요청하는 객체
mycursor = conn.cursor()

try:
    mycursor.execute("drop table inchon")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''CREATE TABLE inchon
             (name text primary key, roadname text, phone text, maindish text)''')


for onedata in range(len(myframe)):
    imsi = myframe.ix[onedata]
    name = imsi['업소명']
    roadname = imsi['소재지 도로명']
    phone = imsi['전화 번호']
    maindish = imsi['주된 음식']
    sql = "insert into inchon values('" + name + "', '" +  roadname + "', '" + phone + "', '" + maindish + "')"
    # print( sql )
    mycursor.execute( sql )

conn.commit()

finddata = '신세계'
sql = "select * from inchon where name like '%" + finddata + "%'"
print('업소명에 [' + finddata + ']라는 글자가 포함된 가게')
for row in mycursor.execute( sql ):
    # print (type(row)) # <class 'tuple'>
    print (row)
print()

finddata = '백숙'
sql = "select * from inchon where maindish like '%" + finddata + "%'"
print('이름에 [' + finddata + ']라는 글자가 포함된 가게')
for row in mycursor.execute( sql ):
    print (row)
print()

sql = "select * from inchon order by name asc"
print('업체 이름순으로 정렬합니다.')
for row in mycursor.execute( sql ):
    print (row)
print()

conn.close()
print()
print('작업 완료^^')