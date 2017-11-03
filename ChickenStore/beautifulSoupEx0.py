from bs4 import BeautifulSoup

# Tag 및 Tag Name 조회
html = "<td class='title'><div class='tit3' id='hong'><a href='www.abcd.com' title='abcd'>미녀와 야수</a></div></td>"
soup = BeautifulSoup(html, 'html.parser')
print( soup )
print()
print( soup.td ) # td가 최상위 이므로 위의 결과와 동일
print()

tag = soup.div 
print( tag )
print()

tag = soup.a 
print( tag )
print()
print( tag.name ) # 해당 태그의 이름
print()

# 속성(Attribute) 값
tag = soup.td
print( tag['class']) # class 속성에 들어 있는 값
print()

tag = soup.div 
print( tag['class']) # class 속성에 들어 있는 값
print( tag.attrs) # 속성들을 사전 형식으로 보여 준다.
print()

tag = soup.find('td', attrs={'class':'title'})
print( tag )
print()

tag = soup.find('div', attrs={'class':'tit3'})
print( tag )

