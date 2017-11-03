import urllib.request
from bs4 import BeautifulSoup

# Tag 및 Tag Name 조회
url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = urllib.request.urlopen( url )
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})

 
print('-' * 30)
print( tags )
print('-' * 30)
print( len(tags) )

print('-' * 30)
print( len(tags) )

print('-' * 30)
for tag in tags :
    print( tag.a.string ) # text 속성도 동일한 결과를 보여 준다.

print('-' * 30)
for tag in tags :
    print( tag.a)
  
print('-' * 30)
atag =  tag.a
for tag in tags :
    print( tag.a.string )
    print( atag['href'] )  
    
    
    
      
    