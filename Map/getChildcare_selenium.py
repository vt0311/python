from bs4 import BeautifulSoup
from selenium import webdriver
from itertools import count

import time
import pandas as pd

def ChildcareAddress(result):

    Childcare_URL = 'http://info.childcare.go.kr/info/pnis/search/NurseryNameSlL.jsp'
    
    wd = webdriver.Chrome('C:\chromedriver_win\chromedriver.exe')
    wd.get(Childcare_URL)
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
    
    
print('Childcare ADDRESS CRAWLING START')
result = []

ChildcareAddress(result)
childcare_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
# childcare_table.sido = childcare_table.sido.apply(lambda v: sido_dict.get(v, v))
# childcare_table.gungu = childcare_table.gungu.apply(lambda v: gungu_dict.get(v, v))
childcare_table.sido[654] = '전라남도'
childcare_table.gungu[654] = '목포시'
childcare_table = childcare_table[childcare_table.sido != ' ']
childcare_table.to_csv("c:/work/childcare_table.csv", encoding="cp949", mode='w', index=True)

print('Childcare ADDRESS CRAWLING END')
