import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import re
import xml.etree.ElementTree as ET

def get_request_url(url, enc='utf-8'):
    
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

'''
<tbody>
    <tr>
        <td class="pdL25">강일지구점</td>
        <td>서울특별시 강동구 아리수로93길 27 202(강일동,,2강일타워2층202호~203호)</td>
        <td class="alignC">02-429-0669</td>
        <td class="alignL"><img src='/images/shop/ico_cafe.png' title='프리미엄카페'>&nbsp;<img src='/images/shop/ico_parking.png' alt='주차가능' title='주차가능'>&nbsp;<img src='/images/shop/ico_family.png' alt='패밀리룸' title='패밀리룸'>&nbsp;<img src='/images/shop/ico_wifi.png' alt='와이파이' title='와이파이'>&nbsp;<img src='/images/shop/ico_gg.png' alt='단체주문' title='단체주문'></td>
        <td class="alignC"><a href="/shop/shop_view.asp?CHAINID=3203" class="f12bG btn8">매장 상세정보</a></td>
    </tr>
    ... (이하 생략)
</tbody>
'''

def getBBQAddress(result):
   
    BBQ_URL = 'https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si='

    rcv_data = get_request_url(BBQ_URL)
    soupData = BeautifulSoup(rcv_data, 'html.parser')

    tbody = soupData.find('tbody')
    
    tr_tag = []

    for store_tr in tbody.findAll('tr'):
        tr_tag = list(store_tr.strings)
        store_name = tr_tag[1]
        store_address = tr_tag[3]
        store_sido_gu = store_address.split()[:2]
            
        result.append([store_name] + store_sido_gu + [store_address])

'''
<table class="table mt20">
<tbody>
	<tr>
	    <td class="t_center">가양동점</td>
	    <td>서울특별시 강서구 강서로74길 12 (가양동)</td>
	    <td class="t_center">
	    02-3663-3700</td>
	    <td class="t_center"><a href="#none" class="button h22 btn_gray" onclick="store_view('126.84170552834682','37.56748111916124','가양동점','02-3663-3700','서울특별시 강서구 강서로74길 12 (가양동)' );">상세정보</a></td>
	</tr>
</tbody>
</table>
'''
def getPelicanaAddress(sido, result):
    
    for page_idx in count():
        
        Pelicana_URL = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=%s&page=%s' % (urllib.parse.quote(sido), str(page_idx + 1))
        print ("[%s] : [%s]" % (sido, str(page_idx + 1)))

        rcv_data = get_request_url(Pelicana_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        
        store_table = soupData.find('table', attrs={'class':'table mt20'})
        tbody = store_table.find('tbody')
        bEnd = True
        for store_tr in tbody.findAll('tr'):
            bEnd = False
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[:2]

            result.append([store_name] + store_sido_gu + [store_address])

        if (bEnd == True):
            return

'''
<lists>
    <item seq="a">
        <aname1>경기가평군가평점</aname1>
        <aname2>경기</aname2>
        <aname3>가평군</aname3>
        <aname4>경기 가평군 가평읍 석봉로</aname4>
        <aname5>경기도가평군가평읍석봉로230</aname5>
        <aname6>031</aname6>
        <aname7>031-581-9982</aname7>
        <aname8>287</aname8>
    </item>
</lists>
'''
def  getNeneAdddress(result):

    Nene_URL = 'http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (urllib.parse.quote('전체'), urllib.parse.quote('전체'))
    
    rcv_data = get_request_url(Nene_URL)

    root = ET.fromstring(rcv_data)
    
    for element in root.findall('item'):
        store_name = element.findtext('aname1')
        store_sido = element.findtext('aname2')
        store_gungu = element.findtext('aname3')
        store_address = element.findtext('aname5')
        
        result.append([store_name] + [store_sido] + [store_gungu] + [store_address])
    
'''
<div class="shopSchList">
	<!-- 매장 리스트 -->
	<ul class="list">
		<li>
			<a href="javascript:mapchange('서울 강동구 고덕동 650-1','고덕1호','541');">
				<dl>
					<dt>고덕1호</dt>
					<dd>
						서울 강동구 고덕동 650-1<br />
						(서울특별시 강동구 고덕로61길 116)<br />
						02 -481-9503~4
					</dd>
				</dl>
			</a>
			<p class="goView" onclick="return location.href='/shop/domestic_sch.asp?shop_id=541&sido1=1&sido2=2'"><img src="../images/shop/bg_btn_shop_on.gif" alt="상세" /></p>
		</li>
	</ul>
	<!-- 지도 -->
	<div class="mapBox" id="itfsMap">
	</div>
</div>
'''
def getKyochonAddress(sido, result):
    
    for sido2 in count():
        Kyochon_URL = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido), str(sido2+1))

        rcv_data = get_request_url(Kyochon_URL)
        if (rcv_data == None):
             return
        soupData = BeautifulSoup(rcv_data, 'html.parser')
    
        ul_tag= soupData.find('ul', attrs={'class': 'list'})
        for store_data in ul_tag.findAll('a', href=True):
            store_name = store_data.find('dt').get_text()
            store_address = store_data.find('dd').get_text().strip().split('\r')[0]
            store_sido_gu = store_address.split()[:2]
            result.append([store_name] + store_sido_gu + [store_address])

'''
<table width="430" border="0" cellpadding="0" cellspacing="1" bgcolor="#E8E8E8">
<tr> 
    <td height="2" colspan="3" bgcolor="#70C5C2"></td>
</tr>
<tr align="center" bgcolor="#DDEFEE"> 
    <td width='80'><b>체인명</b></td>
    <td><b>주소</b></td>
    <td width='100'><b>전화번호</b></td>
</tr>
<tr align="center" bgcolor="#FFFFFF"> 
    <td>강화남산점<br></td>
    <td align='left'>인천시 강화군 강화읍 충렬사로 57</td>
    <td>032-933-2201<br/></td>
</tr>
</table>
'''
def CheogajipAddress(result):
    
    for page_idx in count():

        Cheogajip_URL = 'http://www.cheogajip.co.kr/establish02_02.html?&search=&keyword=&page=%s' % str(page_idx+1)

        
    
        print (Cheogajip_URL)
        response = urllib.request.urlopen(Cheogajip_URL)
        soupData = BeautifulSoup(response.read().decode('CP949'), 'html.parser')

        store_trs = soupData.findAll('tr', attrs={'align': 'center', 'bgcolor':'#FFFFFF'})

        if (store_trs):
            for store_tr in store_trs:
                tr_tag = list(store_tr.strings)
                if (tr_tag[1].count('[휴점]') == 0):
                    store_name = tr_tag[1]
                    store_address = tr_tag[3]
                    store_sido_gu = store_address.split()[:2]
                    result.append([store_name] + store_sido_gu + [store_address])
        else:
            break

        '''
        rcv_data = get_request_url(Cheogajip_URL, 'CP949')
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        for store_tr in soupData.findAll('tr', attrs={'align': 'center', 'bgcolor':'#FFFFFF'}):
            tr_tag = list(store_tr.strings)
            if (tr_tag[1].count('[휴점]') == 0):
                store_name = tr_tag[1]
                store_address = tr_tag[3]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + store_sido_gu + [store_address])
        '''
'''
from selenium import webdriver
<tbody id="store_list">
    <tr class="on lows" idx="788" onclick="store.viewdt(\'788\',\'37.2755111612\',\'127.070853941\');" id="788">
        <td>흥덕지구점<span><!--031-651-9294--></span></td>
        <td class="store_phone">...</td>
        <td class="t_left"><a href="javascript:void(0);">경기도 용인시 기흥구  흥덕1로 79번길 9, 105호</a>...</td>
    </tr>
    <tr class=" lows" idx="630" onclick="store.viewdt(\'630\',\'37.5874473397\',\'128.3221012853\');" id="630">
        <td>휘닉스점<span><!--031-651-9294--></span></td>
        <td class="store_phone"><a href="javascript:void(0);" onclick="store.teldt(\'033-332-8292\');">033-332-8292</a></td>
        <td class="t_left"><a href="javascript:void(0);">강원도 평창군 봉평면 무이리 694-14번지 1층</a><p><i class="online on">온라인</i><i class="coupon on">e-쿠폰</i><!--<i class="cesco on">세스코</i>--><i class="card_dis ">카드할인</i>\t\t</p>\t</td>
    </tr>
</tbody>
'''

from selenium import webdriver
import time
def GoobneAddress(result):

    Goobne_URL = 'http://www.goobne.co.kr/store/search_store.jsp'
    
    wd = webdriver.Chrome('d:/Program Files/Python/WebDriver/chromedriver.exe')
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

        '''
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
        '''
'''
<table class="register01" summary="">
	<colgroup>
		<col width="225" />
		<col width="*" />
		<col width="100" />
	</colgroup>
	<tbody>
		<tr>
			<td class="pt10 pb10">               
				<img src="http://www.bhc.co.kr/images/location/BHC_order.jpg" alt="" style="width: 200px; height: 110px; " />
			</td>
			<td>
				<p>
					<a class="f18" href="javascript:void(0);" onclick="mapwin('37.5521366','126.8710265','(뉴)염창점')">(뉴)염창점 </a>
				</p>
				<p class="mt10 mb10">
					<span class="bold">주소</span> : 서울 강서구 염창동 246-9<br />
					<span class="bold">전화번호</span> : 02-3661-9282
				</p>
			</td>
			<td><a href="javascript:void(0);" onclick="mapwin('37.5521366','126.8710265','(뉴)염창점')"><img src="../../images/button/btn_map.gif" alt="" /></a>
            </td>
		</tr>
    </tbody>
</table>
	

'''
def BhcAddress():
    result = []

    BHC_URL = 'https://www.bhc.co.kr/location/search.asp'
    
    wd = webdriver.Firefox()
    wd.get(BHC_URL)
    time.sleep(10)

    for page_idx in count():
        
        wd.execute_script("goPage('%s')" % str(page_idx + 1))
        print ("PageIndex [%s] Called" % (str(page_idx + 1)))

        time.sleep(2)

        rcv_data = wd.page_source
        
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        
        for store_list in soupData.find('tbody'):
            for store_tr in store_list:
                a_tag = store_tr.findAll('a', attrs={'class': 'f18'})
                if a_tag != None:
                    store_name = a_tag.get_text()
                p_tag = store_tr.find('p', attrs={'class': 'bold'})
                if p_tag != None:
                    store_address = p_tag[0]
            '''        
            tr_tag = list(store_tr.strings)
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                   return result
                store_name = tr_tag[1]
                store_address = tr_tag[6]
                store_sido_gu = store_address.split()[:2]

                result.append([store_name] + store_sido_gu + [store_address])
            '''
    #사실 무의미    
    return result
    
def main():
    
    result = []

    sido_list = ['서울특별시','부산광역시','대구광역시','제주특별자치도','광주광역시',
            '울산광역시','인천광역시','세종특별자치시','경기도','강원도','경상북도',
            '경상남도','충청북도','충청남도','전라북도','전라남도','대전광역시']
    

    sido_list1 = ['서울', '경기', '인천', '강원', '충북', '충남', '경북',
            '경남', '대전', '대구', '전북', '전남', '광주', '울산', '부산',
            '제주', '세종']

    sido_alias = """서울시:서울특별시 서울:서울특별시 강원:강원도 경기:경기도 충남:충청남도  
                    충북:충청북도 경남:경상남도 경북:경상북도 전남:전라남도 전북:전라북도 
                    제주도:제주특별자치도 제주:제주특별자치도 제주시:제주특별자치도
                    세종시:세종특별자치시 세종:세종특별자치시
                    대전시:대전광역시 대전:대전광역시 대구시:대구광역시 대구:대구광역시
                    인천시:인천광역시 인천:인천광역시 광주시:광주광역시 광주:광주광역시
                    울산시:울산광역시 울산:울산광역시 부산시:부산광역시 부산:부산광역시"""
    sido_dict = dict(aliasset.split(':') for aliasset in sido_alias.split())

    gungu_alias = """고양시일산서구:고양시 고양시덕양구:고양시 고양시일산동구:고양시
                    부천시오정구:부천시 부천시소사구:부천시 부천시원미구:부천시
                    안산시단원구:안산시 안산시상록구:안산시
                    안양시동안구:안양시 안양시만안구:안양시
                    성남시중원구:성남시 성남시중원구:성남시 성남시분당구:성남시 성남시수정구:성남시 
                    양편군:양평군 여주군:여주시
                    수원시권선구:수원시 수원시장안구:수원시 수원시권선구:수원시 수원시영통구:수원시 수원시팔달구:수원시
                    용인시기흥구:용인시 용인시수지구:용인시 용인시처인구:용인시
                    포항시북구:포항시 포항시남구:포항시
                    창원시마산회원구:창원시 마산회원구:마산시 창원시진해구:창원시 진해시:창원시
                    창원시마산합포구:창원시 창원시회원구:창원시 창원시성산구:창원시 창원시의창구:창원시
                    상주시낙양동:상주시 상주시사벌면:상주시
                    청주시흥덕구:청주시 청주시서원구:청주시 청주시상당구:청주시 청주시청원구:청주시
                    천안시서북구:천안시 천안시동남구:천안시 
                    전주시덕진구:전주시 전주시완산구:전주시
                    성주읍:성주군 의성읍:의성군 강화읍:강화군 웅진군:옹진군
                    구좌읍:제주시 북제주군:제주시 신광로:제주시 용문로:제주시 천수로:제주시
                    군포시금정동79-1:군포시 군포시금정동79-1:군포시
                    세종특별자치시:세종시 조치원읍:세종시 
                    한솔동:세종시 도담동:세종시 도움3로:세종시 도움8로:세종시
                    나리로:세종시 갈매로:세종시 마음로:세종시 보듬3로:세종시 
                    소담1로:세종시 호려울로:세종시 누리로:세종시 달빛로:세종시
                    연기면:세종시 연동면:세종시 전의면:세종시
                    금남면:세종시 부강면:세종시 연서면:세종시 장군면:세종시
                    전동면:세종시
                    """
    gungu_dict= dict(aliasset.split(':') for aliasset in gungu_alias.split())
 
    print('BBQ ADDRESS CRAWLING START')
    getBBQAddress(result)
    bbq_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    
    bbq_table.sido = bbq_table.sido.apply(lambda v: sido_dict.get(v, v))
    bbq_table.gungu = bbq_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    bbq_table = bbq_table.reset_index().drop_duplicates(subset='store', keep='first').set_index('index')
    
    bbq_table.to_csv("d:/temp/chicken_data/bbq_table.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('BBQ ADDRESS CRAWLING END')

    print('PERICANA ADDRESS CRAWLING START')
    sido_list[3] = '제주도'
    
    for sido in sido_list:
        getPelicanaAddress(sido, result)
    pericana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    
    pericana_table.sido = pericana_table.sido.apply(lambda v: sido_dict.get(v, v))
    pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    pericana_table.to_csv("d:/temp/chicken_data/pericana_table.csv", encoding="cp949", mode='w', index=True)
    sido_list[3] = '제주특별자치도'
    del result[:]
    print('PERICANA ADDRESS CRAWLING END')

    print('NENE ADDRESS CRAWLING START')
    for sido in sido_list1:
        getNeneAdddress(result)
    nene_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    nene_table.sido = nene_table.sido.apply(lambda v: sido_dict.get(v, v))
    nene_table.gungu = nene_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    nene_table.to_csv("d:/temp/chicken_data/nene_table.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('NENE ADDRESS CRAWLING START')

    print('KYOCHON ADDRESS CRAWLING START')
    i = 0
    for sido in sido_list:
        i = i + 1
        getKyochonAddress((i), result)
    kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    kyochon_table.sido = kyochon_table.sido.apply(lambda v: sido_dict.get(v, v))
    kyochon_table.gungu = kyochon_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    kyochon_table = kyochon_table.reset_index().drop_duplicates(subset='store_address', keep='first').set_index('index')
    kyochon_table.to_csv("d:/temp/chicken_data/kyochon_table.csv", encoding="cp949", mode='w', index=True)
    del result[:]
    print('KYOCHON ADDRESS CRAWLING END')
    
    print('CHEOGAJIP ADDRESS CRAWLING START')
    CheogajipAddress(result)
    cheogajip_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    cheogajip_table.sido = cheogajip_table.sido.apply(lambda v: sido_dict.get(v, v))
    cheogajip_table.gungu = cheogajip_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    #주소 수정
    cheogajip_table.sido[38] = '경상북도'
    cheogajip_table.gungu[38] = '영주시' 
    cheogajip_table.sido[61] = '전라남도'
    cheogajip_table.gungu[61] = '여수시'
    cheogajip_table.sido[74] = '경기도'
    cheogajip_table.gungu[74] = '파주시'
    cheogajip_table.sido[81] = '충청북도'
    cheogajip_table.gungu[81] = '청주시'
    cheogajip_table.sido[173] = '경기도'
    cheogajip_table.gungu[173] = '수원시'
    cheogajip_table.sido[174] = '경기도'
    cheogajip_table.gungu[174] = '수원시'
    cheogajip_table.sido[175] = '서울특별시'
    cheogajip_table.gungu[175] = '강남구'
    cheogajip_table.store_address[175] = '서울특별시 강남구 논현동 187-1'
    cheogajip_table.sido[190] = '경기도'
    cheogajip_table.gungu[190] = '오산시'
    cheogajip_table.sido[332] = '경기도'
    cheogajip_table.gungu[332] = '고양시'
    cheogajip_table.sido[926] = '경상남도'
    cheogajip_table.gungu[926] = '함안군'
    cheogajip_table.sido[883] = '경상남도'
    cheogajip_table.gungu[883] = '창원시'
 
    cheogajip_table.to_csv("d:/temp/chicken_data/cheogajip_table.csv", encoding="cp949", mode='w', index=True)

    del result[:]
    print('CHEOGAJIP ADDRESS CRAWLING END')
    
    print('GOOBNE ADDRESS CRAWLING START')
    GoobneAddress(result)
    goobne_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    goobne_table.sido = goobne_table.sido.apply(lambda v: sido_dict.get(v, v))
    goobne_table.gungu = goobne_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    goobne_table.sido[654] = '전라남도'
    goobne_table.gungu[654] = '목포시'
    goobne_table = goobne_table[goobne_table.sido != ' ']
    goobne_table.to_csv("d:/temp/chicken_data/goobne_table.csv", encoding="cp949", mode='w', index=True)
    print('GOOBNE ADDRESS CRAWLING END')
    
    '''
    bhc_addr.append(pd.DataFrame(BhcAddress(), columns=('store', 'sido', 'gungu', 'store_address')))
    print(bhc_addr)
    '''

if __name__ == '__main__':
     main()


'''
function search(){
	sido1 = $("#sido1").val();
	sido2 = $("#sido2").val();

	stringtxt = $("#txt_search").val();
	var intlength = stringtxt.length;
	if (stringtxt.substr(-1) == "점" || stringtxt.substr(-1) == "역") {
		sido3 = stringtxt.substr(0, intlength-1);
	} else {
		sido3 = stringtxt;
	}
	//sido3 = $("#txt_search").val();

	//location.href = "domestic.asp?sido1=" + $("#sido1").val() + "&sido2=" + $("#sido2").val() + "&txtsearch=" + escape($("#txt_search").val());
	location.href = "domestic.asp?sido1=" + $("#sido1").val() + "&sido2=" + $("#sido2").val() + "&txtsearch=" + escape(sido3);
}
$.ajax({
	url: "/common/xml/district/sido.xml",
	dataType: 'text',
	success: function(data) {

		var sd = $(data).find("sidonm");
			sd.each(function(i){
				$(".shopSch .selType02 .selectCus").eq(0).append('<option value="'+(i+1)+'">'+$(this).text()+'</option>')

			if (i == ($(data).length - 1)) {
				bindNextS()
			}
		});

		$('#sido1').val('0').trigger('change');

	},
	error: function() {
		alert("error");
	}
});

<list>
  <sidolist>
    <sido>11</sido>
    <sidonm>서울</sidonm>
  </sidolist>
  <sidolist>
    <sido>26</sido>
    <sidonm>부산</sidonm>
  </sidolist>
  ... (이하 중략)
</list>
'''
'''
for sido1 in range(1, 18):
    for sido2 in count():
        Kyochon_URL = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido1), str(sido2 +1))
        print (Kyochon_URL)
        try:
            html = urllib.request.urlopen(Kyochon_URL)
            soupData = BeautifulSoup(html, 'html.parser')
		
            ul_tag= soupData.find('ul', attrs={'class': 'list'})
            for store_data in ul_tag.findAll('a', href=True):
                store_name = store_data.find('dt').get_text()
                store_address = store_data.find('dd').get_text().strip().split('\r')[0]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + store_sido_gu + [store_address])
        except:
            break
'''