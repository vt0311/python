import urllib.request
import math
import json 
import datetime

access_key="B0j5Y8uG%2BITVQjevfaruHpr%2BwyaLKDGlvOx8Il99C8R1kcLU%2FxmdpuORn8pM0fc3gmSoyNoBvNoHHF%2BGFLYyHQ%3D%3D"

def get_request_url(url):
    
    req = urllib.request.Request(url)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
#             print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
        
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE 2]
def getTourPointData(item, yyyymm, jsonResult):
    # item이라는 사전의 key 목록에서 'addrCd'가 존재하면 챙기고, 없으면 0이라는 값을 선택하라
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd'] # 지역 코드(예 : 1111)
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm'] # 관광지(예 : 종로구)
    rnum = 0 if 'rnum' not in item.keys() else item['rnum'] # 관광지 코드
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt'] # 외국인 방문객
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt'] # 내국인 방문객
    
    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd,
                    'gungu': gungu, 'sido': sido, 'resNm': resNm, 
                    'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})
    return

#[CODE 1]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):
    # yyyymm : 6자리의 년월에 해당하는 날짜
    # sido : 시도(예 : 서울특별시)
    # gungu : 구군
    # nPagenum : 페이지 번호
    # nItems : 조회할 최대 행수(레코드 수) 
    
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    
    # config.py 파일 안에 access_key 변수가 정의 되어 있다.
    parameters = "?_type=json" # 
    parameters += "&serviceKey=" + access_key # 
    parameters += "&YM=" + yyyymm # 년월
    parameters += "&SIDO=" + urllib.parse.quote(sido) # 시도 
    parameters += "&GUNGU=" + urllib.parse.quote(gungu) # 군구(예 : 종로구)
    parameters += "&RES_NM=" # 관광지(예 : 경복궁)
    parameters += "&pageNo=" + str(nPagenum) # 페이지 번호 
    parameters += "&numOfRows=" + str(nItems) # 조회 최대 행수(레코드 수)

    url = end_point + parameters
    
#     print( '유알엘')
#     print( url )
#     print('-----------')    

    retData = get_request_url(url)
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)


def main():

    jsonResult = [] # 결과를 저장할 리스트

    sido = '서울특별시'
    gungu = ''
#     nPagenum = 1 # 페이지 번호
    nTotal = 0 # 조회된 관광지 갯수
    nItems = 100 # 조회할 최대 행수(레코드 수)
    
    nStartYear = 2011 # 검색 시작 년도
    nEndYear = 2017 # 검색 끝 년도
    
#     print("{0}{1:0>2}".format, str(1), str(2))
    
    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            # yyyymm : 201101 부터 201612 까지
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
#             print( yyyymm )

            nPagenum = 1 # 페이지 번호
            
            #[CODE 3]
            while True:
                # jsonData : 특정 지역의 1개월치의 정보를 담아 두기 위한 변수
                # 예시 : 종로구의 2017/11의 데이터
                jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)
                # jsonData 출력 결과 : 하단 주석 참조  
#                 print( jsonData ) 

                if (jsonData['response']['header']['resultMsg'] == 'OK'):
                    nTotal = jsonData['response']['body']['totalCount']
            
                    if nTotal == 0: # 관광지 갯수가 0이면
                        break

#                     print('요소 목록 :')
#                     print( jsonData['response']['body']['items']['item'])

                    # 한개의 관광지 정보를 사전으로 담고 있는 리스트 이다.  (하단 주석 참조)  
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item, yyyymm, jsonResult)
            
                    nPage = math.ceil(nTotal / 100)
                    if (nPagenum == nPage): # 마지막 페이지에서는 멈추도록(hsw)
                        break

                    nPagenum += 1
                
                else:
                    break                

    with open('%s_관광지입장정보_%d_%d.json' % (sido, nStartYear, nEndYear-1), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                        indent=4, sort_keys=True,
                        ensure_ascii=False)
        outfile.write(retJson)
         
    print ('%s_관광지입장정보_%d_%d.json SAVED' % (sido, nStartYear, nEndYear-1))            


if __name__ == '__main__':
    main()
####################################################################################    
'''jsonData 출력 예시 : 교재 122쪽
    {'response': 
        {'header': 
            {
                'resultCode': '0000', 
                'resultMsg': 'OK'
            }, 
            'body': 
                {'numOfRows': 100, 
                'totalCount': 16, 
                    'items': 
                        {'item': [
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 52796, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 1, 'csNatCnt': 52876, 'resNm': '창덕궁'}, 
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 1999, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 2, 'csNatCnt': 9755, 'resNm': '운현궁'}, 
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 168712, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 3, 'csNatCnt': 202572, 'resNm': '경복궁'},
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 3565, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 4, 'csNatCnt': 26882, 'resNm': '창경궁'}, 
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 20343, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 5, 'csNatCnt': 12345, 'resNm': '종묘'}, 
                            {'ym': 201208, 'addrCd': 1117, 'csForCnt': 20914, 'sido': '서울특별시', 'gungu': '용산구', 'rnum': 6, 'csNatCnt': 434529, 'resNm': '국립중앙박물관'}, 
                            {'ym': 201208, 'addrCd': 1111, 'csForCnt': 2175, 'sido': '서울특별시', 'gungu': '종로구', 'rnum': 7, 'csNatCnt': 181507, 'resNm': '서울역사박물관'}, 
                            {'ym': 201208, 'addrCd': 1114, 'csForCnt': 14081, 'sido': '서울특별시', 'gungu': '중구', 'rnum': 8, 'csNatCnt': 45103, 'resNm': '덕수궁'}, 
                            {'ym': 201208, 'rnum': 9, 'resNm': '서울시립미술관 본관', 'sido': '서울특별시', 'gungu': '중구', 'addrCd': 1114, 'csNatCnt': 156966}, 
                            {'ym': 201208, 'addrCd': 1135, 'csForCnt': 121, 'sido': '서울특별시', 'gungu': '노원구', 'rnum': 10, 'csNatCnt': 1714, 'resNm': '태릉 ·  강릉 · 조선왕릉전시관'}, 
                            {'ym': 201208, 'addrCd': 1141, 'csForCnt': 8401, 'sido': '서울특별시', 'gungu': '서대문구', 'rnum': 11, 'csNatCnt': 82241, 'resNm': '서대문형무소역사관'}, 
                            {'ym': 201208, 'rnum': 12, 'resNm': '서대문자연사박물관', 'sido': '서울특별시', 'gungu': '서대문구', 'addrCd': 1141, 'csNatCnt': 43775}, 
                            {'ym': 201208, 'rnum': 13, 'resNm': '트릭아이미술관', 'sido': '서울특별시', 'gungu': '마포구', 'addrCd': 1144}, 
                            {'ym': 201208, 'addrCd': 1165, 'csForCnt': 527, 'sido': '서울특별시', 'gungu': '서초구', 'rnum': 14, 'csNatCnt': 1593, 'resNm': '헌릉ㆍ인릉'}, 
                            {'ym': 201208, 'addrCd': 1168, 'csForCnt': 4672, 'sido': '서울특별시', 'gungu': '강남구', 'rnum': 15, 'csNatCnt': 17434, 'resNm': '선릉·정릉'}, 
                            {'ym': 201208, 'addrCd': 1171, 'csForCnt': 81427, 'sido': '서울특별시', 'gungu': '송파구', 'rnum': 16, 'csNatCnt': 594598, 'resNm': '롯데월드'}]}, 
                        'pageNo': 1}}}

'''    
    
    
''' jsonData['response']['body']['items']['item']의 출력 결과
요소 목록 :
[
    {'addrCd': 1111, 'rnum': 1, 'sido': '서울특별시', 'resNm': '창덕궁', 'csForCnt': 52775, 'ym': 201209, 'csNatCnt': 76660, 'gungu': '종로구'}, 
    {'addrCd': 1111, 'rnum': 2, 'sido': '서울특별시', 'resNm': '운현궁', 'csForCnt': 3209, 'ym': 201209, 'csNatCnt': 34242, 'gungu': '종로구'}, 
    {'addrCd': 1111, 'rnum': 3, 'sido': '서울특별시', 'resNm': '경복궁', 'csForCnt': 106412, 'ym': 201209, 'csNatCnt': 296957, 'gungu': '종로구'}, 
    {'addrCd': 1111, 'rnum': 4, 'sido': '서울특별시', 'resNm': '창경궁', 'csForCnt': 2736, 'ym': 201209, 'csNatCnt': 42107, 'gungu': '종로구'}, 
    {'addrCd': 1111, 'rnum': 5, 'sido': '서울특별시', 'resNm': '종묘', 'csForCnt': 22209, 'ym': 201209, 'csNatCnt': 13121, 'gungu': '종로구'}, 
    {'addrCd': 1117, 'rnum': 6, 'sido': '서울특별시', 'resNm': '국립중앙박물관', 'csForCnt': 13725, 'ym': 201209, 'csNatCnt': 219211, 'gungu': '용산구'}, 
    {'addrCd': 1111, 'rnum': 7, 'sido': '서울특별시', 'resNm': '서울역사박물관', 'csForCnt': 1666, 'ym': 201209, 'csNatCnt': 175273, 'gungu': '종로구'}, 
    {'addrCd': 1114, 'rnum': 8, 'sido': '서울특별시', 'resNm': '덕수궁', 'csForCnt': 11711, 'ym': 201209, 'csNatCnt': 49013, 'gungu': '중구'}, 
    {'addrCd': 1114, 'rnum': 9, 'sido': '서울특별시', 'resNm': '서울시립미술관 본관', 'ym': 201209, 'csNatCnt': 79396, 'gungu': '중구'}, 
    {'addrCd': 1135, 'rnum': 10, 'sido': '서울특별시', 'resNm': '태릉 ·  강릉 · 조선왕릉전시관', 'csForCnt': 64, 'ym': 201209, 'csNatCnt': 3278, 'gungu': '노원구'}, 
    {'addrCd': 1141, 'rnum': 11, 'sido': '서울특별시', 'resNm': '서대문형무소역사관', 'csForCnt': 6102, 'ym': 201209, 'csNatCnt': 24364, 'gungu': '서대문구'}, 
    {'addrCd': 1141, 'rnum': 12, 'sido': '서울특별시', 'resNm': '서대문자연사박물관', 'ym': 201209, 'csNatCnt': 21241, 'gungu': '서대문구'}, 
    {'addrCd': 1144, 'rnum': 13, 'sido': '서울특별시', 'resNm': '트릭아이미술관', 'ym': 201209, 'gungu': '마포구'}, 
    {'addrCd': 1165, 'rnum': 14, 'sido': '서울특별시', 'resNm': '헌릉ㆍ인릉', 'csForCnt': 374, 'ym': 201209, 'csNatCnt': 3848, 'gungu': '서초구'}, 
    {'addrCd': 1168, 'rnum': 15, 'sido': '서울특별시', 'resNm': '선릉·정릉', 'csForCnt': 5628, 'ym': 201209, 'csNatCnt': 32681, 'gungu': '강남구'}, 
    {'addrCd': 1171, 'rnum': 16, 'sido': '서울특별시', 'resNm': '롯데월드', 'csForCnt': 38382, 'ym': 201209, 'csNatCnt': 394611, 'gungu': '송파구'}
]
'''