# 참조 사이트  http://blog.naver.com/93immm/220914230643
# 네이버 카툰들의 제목과 주소를 크롤링해본다.
# 크롤링 사이트 이미지 주소 긁어오기

# urllib2 — extensible library for opening URLs
from urllib.request import  urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame
import os, shutil

weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일10', \
                'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

myfolder = 'c:\\imsi\\'
try:
    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        if os._exists( mypath ):
            shutil.rmtree( mypath )
        os.mkdir( mypath ) # 요일 폴더 생성
except FileExistsError as err:
    pass # 오류를 무시하고 넘긴다.

def saveFile( image_url, weekday, mytitle ) :
    # image_url : 웹 상에 존재하는 다운로드할 이미지 경로 + 이름
    image_file = urlopen( image_url )
    # print()

    myfile = open('c:\\imsi\\' + weekday_dict[ weekday ] \
                  + '\\' +  mytitle + '.jpg', 'wb')
    myfile.write( image_file.read() )

myurl = 'http://comic.naver.com/webtoon/weekday.nhn'

# 이 페이지에 request해서 데이터를 가져온 후 변수에 저장한다.
response = urlopen(myurl)

# BeautifulSoup()를 이용해서 데이터를 파싱한다.
result  = BeautifulSoup(response, 'html.parser')#, from_encoding='UTF-8')
# print( type(response)) # <class 'http.client.HTTPResponse'>
# print(soup.prettify())

mytarget = result.find_all("div", { "class" : "thumb"})

mylist = []
# for문을 이용해서 가공한 데이터를 출력한다.
for abcd in mytarget :
    headerstr = 'comic.naver.com'
    atag = abcd.find('a')
    myhref =  atag.attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    # ------------------------------------------------------------
    imgtag = abcd.find('img')
    mytitle = imgtag.attrs['title'].strip() # 만화 제목
    mytitle = mytitle.replace('?', '').replace(':', '')
    mysrc = imgtag.attrs['src'] # 다운 받을 이미지 경로 + 이름
    # print( mytitleid, end =' ')
    # print( myweekday, end=' ')
    # print( mytitle, end=' ')
    # print( mysrc, end=' ')
    # print( )
    mytuple = ( mytitleid, myweekday, mytitle, mysrc )
    mylist.append( mytuple )
    saveFile( mysrc, myweekday, mytitle)

myframe = DataFrame(mylist, \
                columns=['타이틀번호', '요일', '제목', '링크'])
# print( myframe )
# myframe[ '요일'] = weekday_dict[ myweekday ]

myframe.to_csv('cartoonlist.csv', encoding='UTF-8')

print('작업 완료')