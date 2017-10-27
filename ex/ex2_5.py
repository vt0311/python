'''
Created on 2017. 10. 26.

@author: acorn
'''

s = 'sequence'

print('길이(크기):', len(s))

print('포함횟수:', s.count('e'))

print('검색위치:', s.find('e'), s.find('e', 3), s.rfind('e'))

print('첫 글자 유무:', s.startswith('s'), s.startswith('a'))

print()

ss='mbc';

print('mbc', id('mbc'), id(ss))

ss='abc';

print('abc', id('abc'), id(ss))

print()
print('슬라이싱----')
print(s[0], s[2:4])
print('s[1:], s[1::2], s[2::3]:',s[1:], s[1::2], s[2::3])
print(s[:3], s[3:])
print(s[-1], s[-4:-1])
print(s[-4:], s[::3])

print()
print('변경 전 : ', id(s))

s = 'fre' + s[2:]

print(s)
print('변경 후 :', id(s))

print()
s2 = 'kbs mbc'
s2 = '' + s2[:4] + 'sbs' +s2[4:] + ''

print(s2)

print('문자열 공백 제거', s2.strip() )

#s3 = s2.split(sep='')
#print(s3)

#print('-'.join(s3))

print()

a='대한민국 만세'
b=a.replace('대한민국', '파이썬')
print()




