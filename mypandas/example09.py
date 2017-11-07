'''
Created on 2017. 11. 6.

09. 극장별 상영 횟수 (파이 차트)

@author: acorn
'''
import pandas as pd
import matplotlib.pyplot as plt

# 그래프 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt']
dfthether = pd.read_csv(thetherfile, names=colnames, header=None )
groupbyData = dfthether.groupby('theater')['cnt']

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels : 원주 외곽에 보여줄 라벨
labels = []

# chartData : 그래프에 표시될 값
chartData = groupbyData.sum()
print(type(chartData))
print(chartData)


myylim = [0, chartData.max() + 5 ]

mytitle = 'Pie Chart Exam'
# myxticks = [ 'a', 'b', 'c']

# labels : 원주 외관에 보여줄 라벨
labels = []
myexplode = (0, 0.1, 0)

for key in chartData.index :
    mydata = key + '(' + str(chartData[key]) + ')'
    labels.append(mydata)
    # explode = explode + ( 0, )
    
mytuple = tuple( labels )
# pie 차트는 color, alpha 사용 불가능
# table=True : 차트에 사용된 데이터를 표 형태로 보여준다.

chartData.plot( kind ='pie', explode = myexplode, labels = mytuple, \
                startangle = 90, autopct = '%1.1f%%', title= mytitle)
# shadow = True,   , legend = True, rot = 15 , ylim = myylim, grid = True)

filename = 'example09.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
