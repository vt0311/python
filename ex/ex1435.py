'''
Created on 2017. 10. 30.

@author: acorn
'''
import re

mylist = ['800905-1049118', '700925-1059119']

regEx = '(\d{6})[-]\d{7}'


pattern = re.compile(regEx)

for item in mylist :
    # sub(바꿀_문자열, 바뀔 문자열) : 다른 문자로 치환
    print(pattern.sub('\g<1>-*******', item)) # 뒤 7자리를 모두 *로 만들어라.