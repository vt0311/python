'''
Created on 2017. 11. 2.

@author: acorn
'''
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib

wordInfo = {'대통령': 10, '박근혜': 40, '최순실': 30, '이명박': 20  }

# 값을 기준으로 키를 역순 정렬한다.
Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(Sorted_Dict_Keys)

# 힌글 역순(라다나가)
Sorted_Dict_Keys2 = sorted(wordInfo.keys(), reverse=True)
print(Sorted_Dict_Keys2)

# 값을 역순 정렬한다.
Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
print(Sorted_Dict_Values)

font_location = 'c:/Windows/fonts/malgun.ttf'

font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

plt.xlabel('주요 단어')
plt.ylabel('빈도 수')
plt.grid(True)

plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

plt.show()
