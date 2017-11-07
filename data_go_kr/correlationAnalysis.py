from matplotlib import font_manager, rc
import math
import json
import matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 

saved_folder = 'c:/work/'

def correlation( x, y ):
    n = len(x)
    vals = range( n )
    
    x_sum = 0.0
    y_sum = 0.0
    
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    
    mul_xy_sum = 0.0 
    
    for i in vals :
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
          
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)
        
    try:
        r = ((n*mul_xy_sum)- (x_sum * y_sum)) / \
            math.sqrt(((n*x_sum_pow) - pow(x_sum, 2)) * ((n*y_sum_pow) - pow(y_sum, 2)))
    except :
        r = 0.0         
        
    return r

r_list = [] # 상관 관계 분석 결과를 저장할 리스트

# scatter() 함수를 이용하여 산점도 그리기 함수
#[CODE 2]
def setScatterGraph( tour_table, visit_table, tourpoint):
    #[CODE 8]
    tour = tour_table[ tour_table['resNm'] == tourpoint ]
    merge_table = pd.merge(tour, visit_table, left_index=True, right_index=True)
#     print( merge_table )

#     if tourpoint == '창덕궁' : 
    mylist = [['china','중국인'], ['japan','일본인'], ['usa','미국인']]
        
    # 이미지를 오픈하는 개념이므로 for 구문 밖에서 한번만 오픈한다.
    fig = plt.figure()   
    
    imsi = []
    imsi.append( tourpoint )
    print( '[' + tourpoint + '] 작업중입니다...') 
    for onedata in mylist:
#         print( nara + '/' + hangul)
        plt.xlabel( onedata[1] + ' 입국수')
        plt.ylabel('외국인 입장객수')
        
        r = correlation( list(merge_table[ onedata[0] ]), list(merge_table['ForNum']) )
        plt.title( tourpoint + '- ' + onedata[1] + ' 상관 관계 분석(' + str(r) + ')')
        plt.scatter(list(merge_table[ onedata[0] ]), list(merge_table['ForNum']), \
                    edgecolor='none', alpha=0.75, s= 6, c='black')
    #         plt.show()
        fig.savefig('./cor_chart/' + tourpoint + '(' + onedata[1] + ').png', dpi = 300)
        
        imsi.append( r ) # 상관 분석 결과를 리스트에 추가
        
    r_list.append( imsi )

def main():
    font_location = 'c:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)
    
    #[CODE 4]
    tpFilename = saved_folder + '서울특별시_관광지입장정보_2011_2016.json' 
    jsonTP = json.loads(open(tpFilename, 'r', encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns={'yyyymm', 'resNm', 'ForNum'})
    tour_table = tour_table.set_index('yyyymm')
#     print( tour_table )

    #[CODE 5]
    resNm = tour_table.resNm.unique()

    #[CODE 6]    
    fv_CFilename = saved_folder + '중국(112)_해외방문객정보_2011_2016.json' 
    jsonFV = json.loads(open(fv_CFilename, 'r', encoding='utf-8').read())
    china_table = pd.DataFrame(jsonFV, columns={'yyyymm', 'visit_cnt'})
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
#     print( china_table )    
    
    fv_JFilename = saved_folder + '일본(130)_해외방문객정보_2011_2016.json' 
    jsonFV = json.loads(open(fv_JFilename, 'r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jsonFV, columns={'yyyymm', 'visit_cnt'})
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
#     print( japan_table )    
    
    fv_UFilename = saved_folder + '미국(275)_해외방문객정보_2011_2016.json' 
    jsonFV = json.loads(open(fv_UFilename, 'r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jsonFV, columns={'yyyymm', 'visit_cnt'})
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
#     print( usa_table )

    #[CODE 7] fv_table : 세 나라의 데이터를 병합 시켜 놓은 파일
    fv_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    fv_table = pd.merge(fv_table, usa_table, left_index = True, right_index = True)
#     print( fv_table )
      
    for tourpoint in resNm :
        setScatterGraph( tour_table, fv_table, tourpoint)
        
#     print( r_list )
    r_table = pd.DataFrame(r_list, columns=('tourpoint', 'china', 'japan', 'usa'))
#     print( r_table )
    
    r_table = r_table.set_index( 'tourpoint')
    
# '서울시립미술관 본관'과 '서대문자연사박물관'은 상관 계수의 값이 0이다.
# 다음과 같이 삭제하도록 한다.
    r_table.drop('서울시립미술관 본관')    
    r_table.drop('서대문자연사박물관')
    
    r_table = r_table.sort_values(by='china', ascending=False)
    
    print( r_table )
    
#     plt.figure()
#     plt.subplot(1, 1, 1)  
#     plt.plot(r_table)
#     plt.show()       

if __name__ == '__main__':
    main()
    print('작업 완료')