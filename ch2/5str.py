'''
Created on 2017. 10. 18.

@author: acorn
'''
str = 'very nice to meet you !!!'

print(str)

print(str.startswith('very'))

print(str.endswith('you'))

print(str.find('meet'))
'''index 개념, length 게념이 있다.'''

print(str.rfind('e'))

print(len(str))

print(str.count('e'))

str = '                    hi '

print('[', str, ']')

'''공백 잘라줌'''
print(str.strip())

print('[', str.lstrip(), ']')
print('[', str.rstrip(), ']')
print('[', str.strip(), ']')


str2 = 'abcde'
print(str2.isalpha()) 
''' 알파벳 ''' # 알파벳 

print(str2.isnumeric())
 # 숫자인지

print(str2.isalnum()) 
# 문자인지 숫자인지

print('================================') 

str3 = '12345'
print(str3.isalpha()) 
''' 알파벳인지? ''' # 알파벳 

print(str3.isnumeric())
 # 숫자인지?

print(str3.isalnum()) 
# 문자인지 숫자인지
