# -*- coding: utf-8 -*-

# import json

# myfile = json.loads(str(open('chosun_facebook_mini01.json')), encoding='utf-8')
# # aaa = open('chosun_facebook_mini01.json')
# # print(type(aaa))
# # myfile = json.load(aaa)
# print(len(myfile))

import json

with open('chosun_facebook_mini01.json', 'r', encoding'utf-8') as chosun:
    mydata = json.load(chosun)

print(mydata)
print(mydata['name'])

for key, value in mydata.items():
    print(key, value)
