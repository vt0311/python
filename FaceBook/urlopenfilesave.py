'''
Created on 2017. 11. 1.
urlopen()으로 파일 저장하기
@author: acorn
'''

import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드 --- (1)
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기 --- (2)
with open(savename, mode = "wb") as f:
    f.write(mem)
    print("저장완료")