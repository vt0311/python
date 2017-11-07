'''
Created on 2017. 11. 7.
상관분석과 상관계수
@author: acorn
'''

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()

matplotlib.rc('font', family=font_name)

height = [100, 120, 130, 140, 150, 160, 170, 180, 190]
foot_size = [200, 205, 210, 220, 230, 250, 270, 280, 285]

plt.scatter(height, foot_size)
plt.xlabel('키(cm)')
plt.ylabel('발크기(mm)')
plt.show()
