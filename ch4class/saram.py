'''
Created on 2017. 10. 30.

@author: acorn
'''
class Student:
    
    hakjum = '' # 멤버변수
    myavg = 0.0 # 멤버변수
    
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def mean(self):
        myavg = (self.kor + self.eng + self.math)/ 3
        return myavg
    
    def sum(self):
        # mysum - 지역변수
        mysum = self.kor + self.eng + self.math
        #print(self.avg)
        
        return mysum
    
    def calc(self):
        score = self.myavg
        if (90 <= score <=100):
            self.hakjum = 'A'
        elif 80 <= score < 90 :
            self.hakjum = 'B'
        elif 70 <= score < 80 :        
            self.hakjum = 'C'
        elif 60 <= score < 70 :        
            self.hakjum = 'D'
        elif 0 <= score < 60 :        
            self.hakjum = 'F'
        else :
            self.hakjum = 'F'
            
    def getHakjum(self):
        #hakjum = calc()
        # self 붙어 있으면 멤버 변수
        return self.hakjum
    
hong = Student('홍길동', 60, 70, 80)

hong.calc() # 학점을 계산하는 메소드
result = hong.getHakjum()
print('학점:', result)

result = hong.mean()
result2 = hong.sum()

print('평균:', result)
print('합계:', result2)


park = Student('박영희', 70, 80, 85)

result = park.mean()
result2 = park.sum()
result3 = park.getHakjum()

print('평균:', result)
print('합계:', result2)
print('학점:', result3)



