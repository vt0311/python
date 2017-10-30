'''
Created on 2017. 10. 30.

@author: acorn
'''

class Pet :
    # self는 클래스 내의 모든 메소드에 1번째에 적는다.
    def __init__(self, name, sleeptime, feed):
        self.name = name #왼쪽은 멤버변수, 오른쪽은 지역변수
        self.sleeptime = sleeptime
        self.feed = feed
    
    def sleep(self):
        print(self.name + '가 '+ str(self.sleeptime)+'시간동안 잠을 잡니다.')
        
    def eat(self):
        print(self.name + '가 ' + self.feed +'을(를) 먹습니다.')