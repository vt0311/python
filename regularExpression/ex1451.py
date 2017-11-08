'''
Created on 2017. 10. 30.
정규표현식과 덧셈

숫자 2개가 연속인 항목 추출하기.
12, 34, 55

이들의 합을 구함.

findall 사용
@author: acorn
'''

import re

ss='1234abc가나다ABC_555_6'

#print(ss[0:2])
#print(ss[2:4])

result = re.findall(r'[0-9]{2}', ss)
print(result)

hap = 0
for item in result :
    hap = hap + int(item)
    
print('총합:', str(hap))    
print('총합:', hap)   

