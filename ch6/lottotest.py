'''
Created on 2017. 10. 20.

@author: acorn
'''

'''
로또 만들기
1<= lotto <= 45
수 6개 저장하기.
중복은 걸러낸다.
'''
import random

list1 = []

while len(list1) < 6 :
    intV = random.randint(1,45)
    flag = 0
    if len(list1) == 0:
        list1.append(intV)
    else:
        for i in list1:
            if i == intV:
                flag = 1
        if flag == 0:
            list1.append(intV)
            
    #list1.append(random.randint(1,45))
print(list1) 
#print(len(list1)) 

#input()


'''
random.choice([1, 2, 3, 4, 5])

random.sample(range(1, 47), 6)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(L)


numbers = []
for i in range(1,46):
    numbers.append(i)

'''
#출처: http://itmemo.tistory.com/386 [IT 지식 데이터베이스]


'''
games = []
for game in range(1,6):
    select = []
    
    for i in range(0,6):
        idx = random.randrange(0,len(numbers))
        select.append(numbers[idx])
        del numbers[idx]
    
    print("game" + str(game) + ": ", end="")
    select = sorted(select)
    games.append(select)
    print(select)
'''

#출처: http://itmemo.tistory.com/386 [IT 지식 데이터베이스]
