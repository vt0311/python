# 유럽 여행 갤러리 크롤링 연습

# 짤방을 다운로드 하기위해서 짤방이 있는 게시물에 들어가서 첨부파일을 다운로드 하면 된다.
# 그렇다는 말은 짤방이 없는 게시물엔 들어갈 필요가 없다는 이야기다.

# urllib2 — extensible library for opening URLs
from urllib.request import  urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

# myurl = 'http://gall.dcinside.com/board/lists/?id=japanese'
myurl = 'http://gall.dcinside.com/board/lists?id=travel_europe'
response = urlopen(myurl)
result  = BeautifulSoup(response, 'html.parser')

# print(soup.prettify())

def saveFile( image_url, filename ) :
    # image_url : 다운로드할 이미지 경로
    # filename : 하드디스크에 저장될 파일 이름
    image_file = urlopen( image_url )
    myfile = open('c:\\imsi\\' + filename, 'wb')
    myfile.write( image_file.read() )

totallist = []

# 이미지 경로의 url이 다르다.
old_address = 'http://image.dcinside.com/download.php'# 이전 주소
new_address = 'http://dcimg2.dcinside.com/viewimage.php'# 바뀔 주소
header_url = 'http://gall.dcinside.com'

# tr 태그를 찾은 다음
trtag = result.find_all("tr", { "class" : "tb"})
for abcd in trtag: # abcd는 tr 태그 중 하나이다.
    sublist = []
    if abcd.find('td', {'class': 't_notice'}).text != '공지' : # 가장 맨 위의 행은 제외하고
        #글번호부터 조회수까지
        mynotice = abcd.find('td', {'class': 't_notice'}).text
        sublist.append( mynotice )
        mysubject = abcd.find('td', {'class': 't_subject'})
        sublist.append( mysubject.text)
        sublist.append(abcd.find('td', {'class': 't_writer'}).text)
        sublist.append(abcd.find('td', {'class': 't_date'}).text)
        sublist.append(abcd.find('td', {'class': 't_hits'}).text)

        # 짤방이 있는 글은 'class': 't_subject'인 항목 중에서
        # 하위 태그 <a class="icon_pic_n"> 항목을 찾아 내면 된다.
        # 앞에 header_url 변수를 누적해줘라.
        innerlink = header_url + mysubject.a.get('href')
        myhtml = urlopen( innerlink )
        innerResult = BeautifulSoup( myhtml, 'html.parser')

        # litag : 하위에 <a> 태그의 href 속성에 그림 정보가 들어 있다.
        litag = innerResult.find_all('li', {'class':'icon_pic'})
        cnt = 1 # 카운터 변수
        for qwert in litag:
            filename = qwert.a.string
            # print('filename : ' + filename)

            image_url = qwert.a.get('href') + '\n'
            # replace : 특정 문자열을 다른 문자열로 치환한다.
            image_url = image_url.replace( old_address, new_address )
            # print( image_url )
            # 저장할 이미지 파일의 이름은 해당 글번호_숫자.jpeg 형식으로 저장하도록 한다.
            saveFile( image_url, str(mynotice) + '_' + str(cnt) + '.jpeg' )
            cnt = cnt + 1
        # print('---------------------')

        totallist.append(sublist)

myframe = DataFrame(totallist)
# print( myframe )
# print()

myframe.to_csv('europeinfo.csv', encoding='UTF-8')

print('작업 완료')