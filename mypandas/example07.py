'''
Created on 2017. 11. 6.

@author: acorn
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.series import Series


# 그래프 한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

thetherfile = 'thether.csv'
colnames = ['id', 'theater', 'cnt']
dfthether = pd.read_csv(thetherfile, names=colnames, header=None, index_col = ['id', 'theater'])


newdfthether = dfthether.unstack('theater')
newdfthether.columns.name = 'hohoho'

#색인의 이름이 x축의 타이틀이 된다.
newdfthether.index.name = 'asdf'

mytitle = 'showing count per theater'
myylim = [0, 35]
myalpha = 0.8

print(newdfthether)

newdfthether.plot(kind='bar', rot = 0, ylim=myylim, title=mytitle, grid = True, alpha = myalpha)

filename = 'example07.png'

plt.savefig( filename, dpi=400, bbox_inches='tight')
 
plt.show()