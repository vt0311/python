from matplotlib import font_manager, rc
import matplotlib
import matplotlib.pyplot as plt 

font_location = 'c:/Windows/fonts/malgun.ttf'
# font_location = 'c:/Windows/fonts/batang.ttc'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name) 

plt.plot([1,2,3,4])
plt.xlabel('x축 한글 표시')
plt.show()