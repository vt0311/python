'''
Created on 2017. 10. 30.
아이디와 메일 찾기
@author: acorn
'''
import re

mylist = ['abc@naver.com', 'aaaa@daum.net']

regex = '@'
pattern = re.compile(regex)

mystr1 = mylist[0]
#print(mystr1)

#mymatch1 = pattern.match(mystr1)
#print(mymatch1)

mylist1 = pattern.findall(mystr1)
#print(mylist1)

#myiter1 = pattern.finditer(mystr1)
#print(myiter1)
for item in mylist :
   print( item)
 
myans1 =  re.split(regex, mystr1)
print(re.split(regex, mystr1))
print()

print('아이디:{}, 메일종류:{}'.format( myans1[0], myans1[1])  )

#print('아이디:{}, 메일종류:{}'.format( myans2[0], myans2[1])  )

    

mystr2 = mylist[0]
#print(mystr2)

for idx in range(len(mylist)) :
    #print(idx)
    pos = pattern.search(mylist[idx])
   # print(pos)
    
    ap = pos.start()
   # print(ap)
    print('아이디:', mylist[idx][:ap]  )
    print('메일종류:{}'.format( mylist[idx][ap+1:])  )
    print('아이디:{}, 메일종류:{}'.format(  mylist[idx][:ap] , format( mylist[idx][ap+1:]) )  )
