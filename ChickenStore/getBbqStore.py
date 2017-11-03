import urllib.request
import datetime
import pandas as pd

from bs4 import BeautifulSoup

saved_folder = 'c:/work/'
result = [] # 비어 있는 리스트

def get_request_url(url, enc='utf-8'):    
    #print( url )
    req = urllib.request.Request(url)

    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            
            try:
                # 읽어 와서 바이트 형식으로 저장
                rcv = response.read()
                
                # decode() 함수 사용 후 객체 형식으로 저장
                ret = rcv.decode(enc)
                
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')    
            
            return ret # 객체를 리턴
            
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getBBQAddress(result):   
    BBQ_URL = 'https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si='

    rcv_data = get_request_url(BBQ_URL)
    soupData = BeautifulSoup(rcv_data, 'html.parser')

    tbody = soupData.find('tbody')
    
    tr_tag = []

    for store_tr in tbody.findAll('tr'):
        print( list(store_tr.strings) )
        
        # list() : 리스트가 아닌 것을 리스트로 만들어 주는 함수
        tr_tag = list(store_tr.strings)
        
        store_name = tr_tag[1]
        #print(store_name)
        store_address = tr_tag[3]
        #print(store_address)
        
        # 전체 주소에서 시도와 구군 정보 가져오기
        store_sido_gu = store_address.split()[:2]
        #print(store_sido_gu)
            
        result.append([store_name] + store_sido_gu + [store_address])

print('BBQ ADDRESS CRAWLING START')

getBBQAddress(result)

bbq_table = pd.DataFrame(\
                         result, \
                         columns=('store', 'sido', 'gungu', 'store_address'))

bbq_table.to_csv(saved_folder + "bbq_table.csv", encoding="cp949", \
                 mode='w', \
                 index=True)

print('BBQ ADDRESS CRAWLING END')