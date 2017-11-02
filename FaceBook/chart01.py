'''
Created on 2017. 11. 2.

@author: acorn
'''
import matplotlib.pyplot as plt


plt.rc('font', family='Malgun Gothic')

plt.figure()

plt.subplot(2, 1, 1)

plt.plot([1,2,3,4],[1,2,3,4])

plt.xlabel('x축')
plt.ylabel('y축')

plt.title('matplotlib 활용')

plt.text(3.5, 3.0, '평균:2.5')

plt.grid(True)
#plt.subplot(2, 1, 2)

#plt.plot([5,6,7,8],[5,6,7,8])



plt.show()