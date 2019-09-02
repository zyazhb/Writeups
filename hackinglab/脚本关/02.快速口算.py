import requests
import re
url= "http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php"
r = requests.session()
res = r.get(url)
formula = re.findall("[0-9*+()]{28}",res.text)
formula = "".join(formula)
#print(formula)
ans=eval(formula)
#print(ans)
data={'v':ans}
key = r.post(url,data=data)
#print(key.text)
key = re.findall("<body>(.*?)</body>",key.text)
print(str(key)[9:-5])
