import requests
import re

url = 'http://119.23.73.3:5001/web10/'
r = requests.session()
r1 = r.get(url)
content = r1.text
#print(content)
#experession = re.search
ans = re.findall('moctf',content)
print(len(ans))



data = {'answer':len(ans)}
flag = r.post(url,data=data)
print(flag.text)

flag = re.findall('moctf{.*}',flag.text)
if flag != []:
    print(flag.text)
