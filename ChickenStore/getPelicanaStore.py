import urllib.request
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count

result = []

def get_request_url(url, enc='utf-8'):    
    #print( url )
    req = urllib.request.Request(url)

    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')    
            
            return ret
            
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getPelicanaAddress(sido, result):    
    for page_idx in count():
#         print( page_idx )
        Pelicana_URL = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=%s&page=%s' % (urllib.parse.quote(sido), str(page_idx + 1))
#         print( Pelicana_URL )
#         print ("[%s] : [%s]" % (sido, str(page_idx + 1)))
 
        rcv_data = get_request_url(Pelicana_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')
         
        store_table = soupData.find('table', attrs={'class':'table mt20'})
        tbody = store_table.find('tbody')
        bEnd = True 
        for store_tr in tbody.findAll('tr'):
            bEnd = False # 
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[:2]
 
            result.append([store_name] + store_sido_gu + [store_address])
    
        # bEnd == True라는 의미는 목록이 하나도 조회 되지 않는 경우를 말한다.
        # page=118, page=119를 비교해보라   
        if (bEnd == True):
            return

print('PERICANA ADDRESS CRAWLING START')

sido_list = ['서울특별시','부산광역시','대구광역시','제주특별자치도','광주광역시',
        '울산광역시','인천광역시','세종특별자치시','경기도','강원도','경상북도',
        '경상남도','충청북도','충청남도','전라북도','전라남도','대전광역시']

for sido in sido_list:
    getPelicanaAddress(sido, result)

pericana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
 
pericana_table.to_csv( "c:/work/pericana_table.csv", encoding="cp949", mode='w', index=True) 

print('PERICANA ADDRESS CRAWLING END')