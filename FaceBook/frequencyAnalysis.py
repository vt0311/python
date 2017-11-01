# 다빈도 명사 추출을 통한 워드 클라우드 그리기
import json
import re
import pytagcloud
import webbrowser 
import matplotlib
import matplotlib.pyplot as plt 

from konlpy.tag import Twitter 
from collections import Counter
from matplotlib import font_manager, rc


def showGraph( wordInfo ):
    font_location = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name) 
    
    plt.xlabel('주요 단어')
    plt.ylabel('빈도 수')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)
    
    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')
    
    plt.show()

def saveWordCloud( wordInfo, filename ):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    pytagcloud.create_tag_image(taglist, filename, \
                                size=(640, 480), fontname='korean', rectangular=False)
    webbrowser.open( filename )

def main():
#     openFileName = 'c:/work/chosun_facebook_mini.json'

    # 조선 일보
#     openFileName = 'c:/work/chosun_facebook_2016-10-01_2017-03-12.json'
#     rfile = open( openFileName, 'r', encoding='utf-8').read()
    
    # JTBC 뉴스    
    openFileName = 'c:/work/jtbcnews_facebook_2016-10-01_2017-03-12.json'
    rfile = open( openFileName, 'r', encoding='utf-8-sig').read()

    cloudImagePath = openFileName + '.jpg'
    
    jsonData = json.loads( rfile )
    message = '' 

    #[code 3]
    for item in jsonData:
        if 'message' in item.keys():
            # 파일 : re_sub.py 파일 참조
            message = message + re.sub(r'[^\w]', '', item['message']) + ''

    print('메시지 : ', message)

    #[code 4]
    nlp = Twitter() 
    nouns = nlp.nouns( message )
    count = Counter( nouns )
    print('count 개수 : ', count )
    
    #[code 5]
    wordInfo = dict()
    for key, value in count.most_common(20):
        if(len(str(key)) > 1 ):
            wordInfo[key] = value 
            print(key, '/', value)
               
    showGraph( wordInfo )
    saveWordCloud( wordInfo, cloudImagePath )
        
if __name__ == '__main__' :
    main()