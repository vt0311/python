'''
Created on 2017. 10. 27.

@author: acorn
'''

def ShowPlus(start, end = 5):
    print(start + end)

ShowPlus(2,3)
ShowPlus(3)

ShowPlus(start=2, end=3)
ShowPlus(end=4, start=3)

print('\n가변 인수 처리')

def Func1(*ar):
    print(ar)
    for i in ar:
        print('음식:', i)
        
Func1('비빔밥', '김밥', '볶음밥')

print('\n사전 처리')
def Func2(w, h, **other):
    print('몸무게 : {}, 키 : {}'.format(w, h))
    print(other)
    
Func2(65, 175, name='강감찬', age=30)

# 사전을 매개변수로 입력할 때는 반드시 **을 붙여줘야 
mydict = {'name':'김말똥', 'age':50, 'address':'마포 공덕동'}
Func2(50, 162, **mydict)

print('\n가변 인자와 사전을 동시에 처리')
def Func3(a, b, *v1, **v2):
    print(a, b)
    print(v1)
    print(v2)
    
Func3(1, 2, 3, 4, 5)
Func3(1, 2, 3, 4, 5, m=6, n=7)