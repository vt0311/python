'''
Created on 2017. 11. 1.

urllib.parse 모듈

@author: acorn
'''

import urllib.parse

def input_query_plus() :
    q = urllib.parse.quote_plus('가나다 라')
    return "&query=" + q 

print('결과1 :', input_query_plus() )

def input_query() :
    q = urllib.parse.quote('가나다 라')
    return "&query=" + q

print('결과2 :', input_query() )
