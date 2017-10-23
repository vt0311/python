'''
Created on 2017. 10. 20.

@author: acorn
'''
from ch7.member import Member
from ch7.member import GuideM
from ch7.member import TravelerM

mList = []


while True:
    menuNo = int(input('0:종료, 1:입력, 2:출력:'))
    
    if(menuNo == 0):  ''' 종료 '''
        break 
    
    elif(menuNo == 1): ''' 입력 '''
        #guideYN = int(input(''))
        memNo = int(input('회원 종류 입력: 1:가이드회원, 2:여행회원'))
       
        if (memNo == 1) :
               # pass
            tmpGM = GuideM()
              
            tmpGM.id = input('아이디를 입력:')
            tmpGM.pwd = input('비번을 입력:')
            tmpGM.mtype = 1
            tmpGM.area = input('여행지역 입력:')
            tmpGM.intro = input('소개를 입력:')
             
            mList.append(tmpGM)
            
        elif (memNo == 2 ) :   
            tmpTM = TravelerM()
        
            tmpTM.id = input('아이디를 입력:')
            tmpTM.pwd = input('비번을 입력:')
            tmpTM.mtype = 2
            tmpTM.mateno = input('여행동료수 입력:')
            tmpTM.tourday = input('여행기간 입력:')
            
            mList.append(tmpTM)
             
        else :
             print('wrong input!!! try again!!!')   
    
    elif(menuNo == 2): ''' 출력 '''
        #pass
        for i in range(len(mList)):
            print(mList[i].chullyuk())
            print(len(mList))
           ''' print(mList[i].pwd)
            print(mList[i].)
            print(mList[i].id)
            print(mList[i].id)'''
            
    
    else:    
        print('wrong input!!! try again!!!')
        
'''    
m1 = Member()
mList.append(m1)
print(mList) 
'''
        
'''
class Member:
    id=''
    pwd=''
    mtype=0 #가이드1, 멤버2
    
class GuideM(Member):
    area=''
    intro=''
class TravelerM(Member):
    mateno=''
    tourday=''
    '''
   
   ''' 
def memberFunc():
    mList = []
    
    
    
for i in range(menuNo):
    print(memberFunc())
    
    if (menuNo == 1) 
    
'''
