'''
Created on 2017. 10. 27.

@author: acorn
'''

a = 10
b = 20
c = 30

print('함수 수행 전 a{}, b{}, c{}'.format(a, b, c))

def Foo():
    a = 40
    b = 50
    print('Foo에서 출력) a:{}, b:{}, c:{}'.format(a,b,c))
    def Bar():
        #b = 60
        #c = 70
        nonlocal b
        global c
        print('Bar에서 출력1) a:{}, b:{}, c:{}'.format(a,b,c))
        #b = 60
        print()
        #c = 70
        print()
    Bar()
    a = 100
    #Foo 함수 내에서 유효함으로 a는 40이 아닌 100 참조
    print('Foo에서 출력) a:{}, b:{}, c:{}'.format(a,b,c))
    
Foo() 
    
print('함수 수행 후  a:{}, b:{}, c:{}'.format(a,b,c))