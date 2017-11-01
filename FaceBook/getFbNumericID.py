# -*- coding: utf-8 -*-

import urllib.request
import json

if __name__ == '__main__':

    # [CODE 1]
    page_name = "jtbcnews"    
    app_id = "1771849489774424" # 개발자 계정으로 얻은 내 앱 아이디
    app_secret = "c1e6029bf13c291dc7f53630d8af14ac" # 개발자 계정으로 얻은 내 앱 시크릿 코드
    access_token = app_id + "|" + app_secret

    # [CODE 2]
    # https://graph.facebook.com/v2.8/[page_id]/?access_token=[App_ID]|[Secret_Key]
    # 형식의 문자열을 만들어 낸다

    base = "https://graph.facebook.com/v2.10"
    node = "/" + page_name
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    # [CODE 3]
    req = urllib.request.Request(url)
    
    # [CODE 4]
    try:
        # urlopen : 네트워크를 통하여 읽은 데이터를 메모리에 올린다.
        response = urllib.request.urlopen(req)
        if response.getcode() == 200: # 서버의 응답 코드(성공)
            
            # read() : 이 메소드를 이용하여 binary() 데이터를 만들어 낸다.
            # decode() : 디코딩을 하여...            
            # json.loads : Json 형식의 문자열을 파이썬의 list 형식으로 변경해준다. 
            data = json.loads(response.read().decode('utf-8'))
            print( 'data :', data )
            
            page_id = data['id']
            name = data['name'] # JTBC 뉴스
            print( 'name :', name )
            print ("%s 페이스 북 Numeric ID : %s" % (page_name, page_id))
    except Exception as e:
        print (e)    
        
        
# 실행 결과
# data : {'name': 'JTBC 뉴스', 'id': '240263402699918'}
# name : JTBC 뉴스
# jtbcnews 페이스 북 Numeric ID : 240263402699918