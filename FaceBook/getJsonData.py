# -*- coding: utf-8 -*-

import json

# myfile = json.loads(str(open('chosun_facebook_mini01.json')), encoding='utf-8')
# # aaa = open('chosun_facebook_mini01.json')
# # print(type(aaa))
# # myfile = json.load(aaa)
# print(len(myfile))


def main():
    openFileName = 'C:/work/jumsu.json'
    rfile = open(openFileName, 'r', encoding='utf-8' ).read()
    jsonData = json.loads(rfile)
    
    print('결과물은 사전을 각 요소로 갖는 list 구조이다.')
    print(jsonData)
    
#with open('chosun_facebook_mini01.json', 'r', encoding'utf-8') as chosun:
#    mydata = json.load(chosun)

#print(mydata)
#print(mydata['name'])

    for oneitem in jsonData:
        # oneitem : 사전 구조의 요소 1개를 의미
        print(oneitem.keys())
        print(oneitem.values())
        print('이름', oneitem['name'])
        print('국어', oneitem['kor'])
        print('영어', oneitem['eng'])
        print('수학', oneitem['math'])
        print('성별', oneitem['gender'])
        
        
        if 'hello' in oneitem.keys():
            message = oneitem['hello']
            print('메시지:', message)
    
if  __name__ == '__main__' :
     main()    
    
