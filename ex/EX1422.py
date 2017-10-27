'''
Created on 2017. 10. 27.

@author: acorn
'''

def DoFunc1():
    print('Do Func1 호출') # 특정값을 반환하지는 않음
    
def DoFunc2(name):
    print('안녕', name)
    # return None   #생략해도 None 반환
    
def DoFunc3(arg1, arg2):
    res = arg1 + arg2
    return res

#-- 여기서부터 함수 호출을 해본다
DoFunc1()
print('딴짓을 하다가')

DoFunc1()
print('함수명은 주소:', DoFunc1)

OtherFunc = DoFunc1
OtherFunc()

print('현재 파일의 객체 목록:', globals())

print()
print(DoFunc2('한국인'))

#pr
#
print(DoFunc2(10))

print()
print(DoFunc3(10, 20))
print(DoFunc3('파이썬', '만세'))

print()
def Area_tri(a,b):
    c = a * b / 2
    Area_print(c)
    
def Area_print(c):
    print('삼각형의 면적은', c)
    
Area_tri(20, 30)    


