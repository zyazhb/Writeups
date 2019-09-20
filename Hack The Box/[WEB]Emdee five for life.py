import requests
import re
import hashlib
while(True):
    url="http://docker.hackthebox.eu:47870/"
    r=requests.session()
    web=r.get(url)
    string=re.findall("[a-zA-Z0-9]{20}",web.text)
    print(string)
    string=hashlib.md5(str(string)[2:-2].encode('utf8')).hexdigest()
    print(string)
    web=r.post(url,data={'hash':string})
    print(web.text)
