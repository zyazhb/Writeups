#日志审计wp by-zya
import re
file = open('日志审计.log')
for i in file:
    flag = re.findall('flag.php\?user\=*',i)
    if(flag):
        text = re.findall('([0-9]{1,3})\-',i)
        text = int("".join(text))
        print(chr(text),end="")
