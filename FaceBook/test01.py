'''
Created on 2017. 11. 1.
파일 다운로드 하기
@author: acorn
'''
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"

savename = "test.png"

urllib.request.urlretrieve(url, savename)

print('저장되었습니다.')