import requests
import re

for i in range(10):
    host="http://123.206.31.85:10020/?key="

    r = requests.session()
    text = r.get(host).text
    key = re.findall("[a-z0-9]{33}",text)
    key ="".join(key)
    #print(key)
    print(host+str(key))
    ans = r.get(host+str(key))
    print(ans.text+"\n")
    i=i+1
