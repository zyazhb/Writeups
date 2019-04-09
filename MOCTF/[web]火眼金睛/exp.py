import requests
import re

url = 'http://119.23.73.3:5001/web10/'
r = requests.session()
r1 = r.get(url)
content = r1.text
#print(content)
#experession = re.search
ans = re.findall('moctf',content)
    '''
    ans=eval(ans)
    print(ans)
    data = {'result':ans}
    flag = r.post(url,data=data)
    print(flag.text)
    #flag = re.findall('Bugku{.*}',flag.text)
    #if flag != []:
    #print(flag.text)
    i=i+1
    '''
