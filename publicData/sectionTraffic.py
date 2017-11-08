import matplotlib.pyplot as plt
import pandas as pd

mycolumn = ['구간', '차종', '1월', '2월', '3월', '4월', '5월', '6월']
filename = 'sectionTraffic.csv'
#myframe = pd.read_csv( filename, encoding='EUC-KR')
myframe = pd.read_csv( filename, encoding='UTF-8')
# print( type(myframe) ) # <class 'pandas.core.frame.DataFrame'>
# print()

# print( myframe )
# print()

print('# 구간별 1~3월 각월별 평균')
mygrouping = myframe.groupby('구간')['1월', '2월', '3월']
result = mygrouping.sum()

print(result)
print()

print('# 차종별 1월의 평균')
mygrouping = myframe.groupby('차종')['1월']
result = mygrouping.mean()

print(result)
print()

col_mapping = {'1월':'January', '2월':'February', '3월':'March', \
    '4월':'April', '5월':'May', '6월':'June'}
mycolumn = ['구간', '차종', '1월', '2월', '3월', '4월', '5월', '6월']

# newframe = myframe[ myframe['구간'] == '서울~신갈JC']
newframe = myframe[ myframe['구간'] == '서남원~구례화엄']

# 필요한 열만 재색인한다.
newframe = newframe.reindex( columns = mycolumn )

# 컬럼 이름을 영문이름으로 맵핑 시킨다.
newframe = newframe.rename( columns = col_mapping )

print( newframe )
print()


mytitle = 'Traffic'
myylim = [0, 200000 ] # y축의 상하한값
myalpha = 0.8

print( newframe )
# newframe.plot(kind='bar', rot = 0, ylim = myylim,
# title = mytitle, grid = True, alpha = myalpha)
newframe.plot(kind='bar', rot = 0, title = mytitle, grid = True, alpha = myalpha)

filename = 'traffic.png'
plt.savefig( filename, dpi=400, bbox_inches='tight')
# plt.show()