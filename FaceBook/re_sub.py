import re

text = '[특종]대한민국 통일됨(후후후)\n\n#조아 #아주 조아 #cheeze'
newtext = re.sub(r'[^\w]', '', text) + ''
print( newtext )