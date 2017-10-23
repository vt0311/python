'''
Created on 2017. 10. 20.

@author: acorn
'''
class Member:
    id=''
    pwd=''
    mtype=0 #가이드1, 멤버2
    def chullyuk(self):
        print('{}\t{}'.format(self.id, self.pwd))

class GuideM(Member):
    area=''
    intro=''
     
    def chullyuk(self):
        super().chullyuk()
        print('{}\t{}'.format(self.area, self.intro))
        
        
class TravelerM(Member):
    mateno=''
    tourday=''
    
    def chullyuk(self):
        super().chullyuk()
        print('{}\t{}'.format(self.mateno, self.tourday), end='')
