from bs4 import BeautifulSoup
from selenium import webdriver
from itertools import count

import time
import pandas as pd

def GoobneAddress(result):

    Goobne_URL = 'http://www.goobne.co.kr/store/search_store.jsp'
    
    wd = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    wd.get(Goobne_URL)
    time.sleep(10)

    for page_idx in count():
        
        wd.execute_script("store.getList('%s')" % str(page_idx + 1))
        print ("PageIndex [%s] Called" % (str(page_idx + 1)))

        time.sleep(5)
 
        rcv_data = wd.page_source
        
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        
        for store_list in soupData.findAll('tbody', attrs={'id': 'store_list'}):
            for store_tr in store_list:
                tr_tag = list(store_tr.strings)
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                   return result
               
                store_name = tr_tag[1]
                if (tr_tag[3] == ''):
                    store_address = tr_tag[5]
                else:
                    store_address = tr_tag[6]
                store_sido_gu = store_address.split()[:2]

                result.append([store_name] + store_sido_gu + [store_address])
    
    
print('GOOBNE ADDRESS CRAWLING START')
result = []

GoobneAddress(result)
goobne_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
# goobne_table.sido = goobne_table.sido.apply(lambda v: sido_dict.get(v, v))
# goobne_table.gungu = goobne_table.gungu.apply(lambda v: gungu_dict.get(v, v))
goobne_table.sido[654] = '전라남도'
goobne_table.gungu[654] = '목포시'
goobne_table = goobne_table[goobne_table.sido != ' ']
goobne_table.to_csv("c:/work/goobne_table.csv", encoding="cp949", mode='w', index=True)

print('GOOBNE ADDRESS CRAWLING END')
