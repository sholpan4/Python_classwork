import re

pattern = r',\s*'
text = 'Oct 10, Sep 3, Arp 4'

result = re.split(pattern, text)
print(result)

pattern2 = r'[A-Za-z]+ [0-9]{2}'
res2= re.sub(pattern2, '*****', text)
print(res2)
