import string

from base64 import *

b=b64decode("aWdxNDs2NDFSOzFpa1I1MWliT08w")
#b=b64decode("RU9CRC43aWdxNDs3NDFSOzFpa1I1MWliT08w")
b="EOBD.igq4;641R;1ikR51ibOO0"
data=list(b)


for k in range(0,200):
    
    key=""

    for i in range(len(data)):

        key+=chr(ord(data[i])^k)

    print key+"\n"

