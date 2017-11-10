import datetime
import urllib.request
import json

client_id = "LaQyj9g37x7Ac6N0rxhK"
client_secret = "YdruZ2tsgK"

#[CODE 1]
def get_request_url(url):
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 3]
def getPostData(post, jsonResult):
    
    title = post['title'] # 제목
    description = post['description'] # 간단한 내용
    org_link = post['originallink']
    link = post['link'] # 링크

    #Tue, 14 Feb 2017 18:46:00 +0900
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    
    jsonResult.append({'title':title, 'description': description, 
                'org_link':org_link, 'link': link, 'pDate':pDate})
    return    

#[CODE 2]
def getNaverSearchResult(sNode, search_text, page_start, display):
    # sNode : 검색을 위한 모드('news', 'blog', 'cafearticle')
    # search_text : 검색 하고자 하는 키워드
    # page_start : 시작 페이지 번호
    # display : 1회 검색시 가져올 행수(레코드 수)
    
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % ( sNode )
    
    # urllib.parse.quote() 함수는 한글을 인코딩해주는 역할이다.
#     print( urllib.parse.quote('탄핵'))
    
    # 교재 p109 참조
    parameters = "?query=%s" % (urllib.parse.quote(search_text))
    parameters += "&start=%s" % (page_start)
    parameters += "&display=%s" % (display) 
    
    url = base + node + parameters
    
    retData = get_request_url(url)
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = [] # 결과를 저장할 리스트

    # 'news', 'blog', 'cafearticle'
    sNode = 'news'
    search_text = '김주혁' # 검색 키워드
    display_count = 100
    
    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
#     print( jsonSearch ) # jsonSearch 결과 파일.txt 참조 요망   
    
    print(jsonSearch['display'])
    while ((jsonSearch != None) and (jsonSearch['display'] != 0)):
#         print('갯수 :', len(jsonSearch['items']))
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)
        
        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
    
    with open('%s_naver_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                        indent=4, sort_keys=True,
                        ensure_ascii=False)
        outfile.write(retJson)
        
    print ('%s_naver_%s.json SAVED' % (search_text, sNode))
    
if __name__ == '__main__':
    main()