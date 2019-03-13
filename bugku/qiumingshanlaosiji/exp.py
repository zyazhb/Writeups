import requests
import re

i=0
while i<10:
    url = 'http://123.206.31.85:10002/'
    r = requests.session()
    r1 = r.get(url)
    content = r1.text
    #print(content)
    #experession = re.search
    ans = re.findall('<br/>\\n(.*?)</p>',content)
    ans = "".join(ans) 
    ans=eval(ans)
    print(ans)
    data = {'result':ans}
    flag = r.post(url,data=data)
    print(flag.text)
    #flag = re.findall('Bugku{.*}',flag.text)
    #if flag != []:
    #print(flag.text)
    i=i+1
