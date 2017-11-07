import pandas as pd
#import datetime
#from itertools import count
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import rcParams, style
from matplotlib import font_manager, rc

def correlation(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0
    
    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)
    
    r = ((n * mul_xy_sum) - (x_sum * y_sum)) / math.sqrt( ((n*x_sum_pow) - pow(x_sum, 2)) * ((n*y_sum_pow) - pow(y_sum, 2)) )

    return r

def concentration(chicken_table):

    plt.figure(figsize=(4, 3))
    
    idx_cols = ['bbq', 'cheogajip', 'goobne', 'kyochon', 'nene', 'pericana']

    for col, label in [('bbq', 'BBQ'), ('cheogajip', 'CEHGAJIP'), ('goobne', "GOOBNE"), ('kyochon', "KYOCHON"), ('nene', "NENE"), ('pericana', "PERICANA")]:
        cumulv = np.cumsum(sorted(chicken_table[col], reverse=True)) / chicken_table[col].sum()
        plt.plot(cumulv, label='{} ({})'.format(label, int(chicken_table[col].sum())))
        
    plt.legend(loc='best')
    plt.xlabel('Number of districts (si/gun/gu)')
    plt.ylabel('Cumulative fraction')
    plt.show()

def storeScatter(data, store1, store2):
    
    plt.scatter(data[store1],
                data[store2],
                edgecolor='none', alpha=0.75, s=6, c='black')
    
    plt.xlim(-1, 40)
    plt.ylim(-1, 40)
    plt.xlabel(store1)
    plt.ylabel(store2)
    
    r = correlation(data[store1], data[store2])
    plt.annotate('r={:.5f}'.format(r), (35, 37.5))

def showMap(blockedMap, targetData, strTitle, strColor, gamma):

    BORDER_LINES = [
        [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
        [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
        [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
        [(9, 12), (9, 10), (8, 10)], # 강원도
        [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
         (13, 4), (14, 4), (14, 2)], # 충청남도
        [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
         (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
        [(14, 4), (15, 4), (15, 6)], # 대전시
        [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도
        [(14, 8), (16, 8), (16, 10), (15, 10),
         (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
        [(15, 11), (16, 11), (16, 13)], # 울산시
        [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
        [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
        [(18, 5), (20, 5), (20, 6)], # 전라남도
        [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
    ]

    whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])
    datalabel = targetData
    
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])
    mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
    cmapname = strColor
    plt.figure(figsize=(8, 13))
    plt.title(strTitle)
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)
    for idx, row in blockedMap.iterrows():
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        dispname = row['shortName']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 7.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=4)

    plt.gca().invert_yaxis()
    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(targetData)
    plt.tight_layout()
    
    plt.savefig('d:/temp/chicken_data/' + targetData + '.png')

    plt.show()

def main():
    
    bbq_table = pd.DataFrame.from_csv('d:/temp/chicken_data/bbq_modify.csv', encoding='CP949', index_col=0, header=0)
    bbq =  bbq_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    pericana_table = pd.DataFrame.from_csv('d:/temp/chicken_data/pericana_modify.csv', encoding='CP949', index_col=0, header=0)
    pericana =  pericana_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    nene_table = pd.DataFrame.from_csv('d:/temp/chicken_data/nene_modify.csv', encoding='CP949', index_col=0, header=0)
    nene =  nene_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    kyochon_table = pd.DataFrame.from_csv('d:/temp/chicken_data/kyochon_modify.csv', encoding='CP949', index_col=0, header=0)
    kyochon =  kyochon_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    cheogajip_table = pd.DataFrame.from_csv('d:/temp/chicken_data/cheogajip_modify.csv', encoding='CP949', index_col=0, header=0)
    cheogajip =  cheogajip_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    goobne_table = pd.DataFrame.from_csv('d:/temp/chicken_data/goobne_modify.csv', encoding='CP949', index_col=0, header=0)
    goobne =  goobne_table.apply(lambda r: r['sido'] + ' ' + r['gungu'], axis=1).value_counts()
    
    data_draw_korea = pd.read_csv('d:/temp/chicken_data/data_draw_korea.csv', index_col=0, encoding='UTF-8')
    data_draw_korea.index = data_draw_korea.apply(lambda r: r['광역시도'] + ' ' + r['행정구역'], axis=1)

    # Merge Table Create
    chicken_table = pd.DataFrame({'bbq': bbq, 'pericana': pericana, 'nene': nene, 'kyochon': kyochon, 'cheogajip': cheogajip, 'goobne': goobne}).fillna(0)
    
    chicken = pd.merge(data_draw_korea, chicken_table, how='outer', left_index=True, right_index=True)
    chicken = chicken[~np.isnan(chicken['면적'])].fillna(0)
    chicken['total'] = chicken_table.sum(axis=1)
    #chicken[np.isnan(chicken['면적'])]
    '''
    idx_cols = ['bbq', 'cheogajip', 'goobne', 'kyochon', 'nene', 'pericana']
    
    chicken.loc['경상남도 창원시', idx_cols] += chicken.loc['경상남도 마산시', idx_cols]
    chicken.loc['경상남도 함양군', idx_cols] += chicken.loc['경상남도 함양', idx_cols]
    chicken.loc['경상남도 합천군', idx_cols] += chicken.loc['경상남도 함천군', idx_cols]
    chicken.loc['경상남도 합천군', idx_cols] += chicken.loc['경상남도 합천', idx_cols]
    chicken.loc['경상북도 포항시', idx_cols] += chicken.loc['경상북도 남구', idx_cols]
    chicken.loc['경상남도 김해시', idx_cols] += chicken.loc['부산광역시 김해시', idx_cols]
    chicken.loc['인천광역시 남동구', idx_cols] += chicken.loc['인천광역시 남동', idx_cols]
    chicken.loc['충청남도 당진시', idx_cols] += chicken.loc['충청남도 당진군', idx_cols]
    chicken.loc['충청북도 청주시', idx_cols] += chicken.loc['충청북도 청원군', idx_cols]

    chicken = chicken[~np.isnan(chicken['면적'])].fillna(0)
    '''
    '''
    #전국 매장수
    chicken_total = chicken_table
    chicken_total['total'] = chicken_total.sum(axis=1)
    chicken_total = chicken_total.sort(columns='total', ascending=False)

    style.use('ggplot')
    rcParams['font.size'] = 12
    plt.figure(figsize=(4, 3))
    chicken_total.sum(axis=0).iloc[:7].plot(kind='bar')
    plt.show()


    #매장별 집중도
    concentration(chicken)

    #상관관계분석    
    plt.figure()
    row = 0
    
    for i in range(0, len(idx_cols)):
        ax = plt.subplot(6, 6, row*6+1)
        storeScatter(chicken, idx_cols[i], 'bbq')
        ax = plt.subplot(6, 6, row*6+2)
        storeScatter(chicken, idx_cols[i], 'cheogajip')
        ax = plt.subplot(6, 6, row*6+3)
        storeScatter(chicken, idx_cols[i], 'goobne')
        ax = plt.subplot(6, 6, row*6+4)
        storeScatter(chicken, idx_cols[i], 'kyochon')
        ax = plt.subplot(6, 6, row*6+5)
        storeScatter(chicken, idx_cols[i], 'nene')
        ax = plt.subplot(6, 6, row*6+6)
        storeScatter(chicken, idx_cols[i], 'pericana')
        row = row + 1

    plt.tight_layout()
    #plt.subplots_adjust(left=0.1, bottom=0.1, right=0.1, top=0.1, wspace=0.2, hspace=0.2)
    plt.show()
    '''

    #치킨 맵
    #if platform.system() == 'Darwin':
    #    rc('font', family='AppleGothic')
    #elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
    
    

    #프렌차이즈별 닭집분포
    showMap(chicken, 'total', '6개 프렌차이즈 통닭집 분포', 'RdPu', 0.75)
    showMap(chicken, 'bbq', 'BBQ 매장 분포', 'Reds', 0.75)
    showMap(chicken, 'cheogajip', '처갓집양념통닭 매장 분포', 'Greens', 0.75)
    showMap(chicken, 'goobne', '굽네치킨 매장 분포', 'Purples', 0.75)
    showMap(chicken, 'kyochon', '교촌치킨 매장 분포', 'Oranges', 0.75)
    showMap(chicken, 'nene', '네네치킨 매장 분포', 'Greys', 0.75)
    showMap(chicken, 'pericana', '페리카나 매장 분포', 'Blues', 0.75)
    
    #인구만명당 치킨집 수
    chicken['total10K'] = chicken['total'] / chicken['인구수'] * 10000
    showMap(chicken, 'total10K', '인구만명당 치킨집 수', 'Reds', 0.75)
    
    #면적당 치킨집 수
    chicken['area'] = chicken['total'] / chicken['면적']
    showMap(chicken, 'area', '면적당 치킨집 수', 'Reds', 0.75)
    
if __name__ == '__main__':
     main()