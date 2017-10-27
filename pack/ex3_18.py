print('방법1 : import 패키지명.모듈명')
import pack.mymod1
print(dir(pack.mymod1)) # mymod1에 정의된 멤버 확인
print(pack.mymod1.__file__)# 경로 명 및 파일 명
print(pack.mymod1.__name__)# 모듈 명
 
print('mymod1의 함수 호출')
list1 = [1, 3]
list2 = [1, 2]
 
pack.mymod1.ListHap(list1, list2)
print('다른 모듈의 전역 변수 : ', pack.mymod1.tot)
 
print('방법2 : from 패키지명 import 모듈명')
from pack import mymod1
mymod1.Kbs()# 모듈명.함수명으로 호출한다.
 
print('방법3 : from 패키지명.모듈명 import 함수명')
from pack.mymod1 import Mbc
Mbc() # 함수명으로 호출한다.
 
print('패키지 경로가 다른 곳에 있는 모듈 읽기')
import pack_other.mymod2
print('패키지명.모듈명.함수명()으로 호출')
re_hap = pack_other.mymod2.Hap(5, 3)
print('합 :', re_hap)
print('차 :', pack_other.mymod2.Cha(5, 3))
 
# PythonPath : C:\Anaconda3\Lib 폴더에 mymod3.py 파일을 미리 복사해둔다.
print('PythonPath가 설정된 폴더의 모듈 읽기 실습')
import mymod3
print('곱1 :', mymod3.Gop(5, 3))
 
from mymod3 import *
print('곱2 :', Gop(10, 5))
 
print('\n\n전혀 연관이 없는 폴더의 모듈 읽기')
print('방법1 : Pythonpath에 해당 폴더를 추가한다.')
print('방법2')
import sys
sys.path.append(r'c:/work')
# run time 시점에 'c:/work'를 읽어 들이므로 문제 없음
# 아래 빨간 줄 무시
import mymod4
print('나누기 :', mymod4.Nanugi(5, 3))
