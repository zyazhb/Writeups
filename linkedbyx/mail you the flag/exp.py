import hashlib
from multiprocessing.dummy import Pool as ThreadPool
import requests
import re

# MD5截断数值已知 求原始数据
# 例子 substr(md5(captcha), 0, 6)=60b7ef

def md5(s):  # 计算MD5字符串
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()

r = requests.session()
url="http://101.71.29.5:10014/"
content = r.get(url).text
print("\n[+]Got content:\n"+content)
pie = re.findall("[a-zA-Z0-9]{4}</center>",content)
pie = "".join(pie)
keymd5 = pie[0:-9]
print("\n[+]Got keymd5:\n"+keymd5)
#keymd5 = ans   #已知的md5截断值
md5start = 0   # 设置题目已知的截断位置
md5length = 4

def findmd5(sss):    # 输入范围 里面会进行md5测试
    key = sss.split(':')
    start = int(key[0])   # 开始位置
    end = int(key[1])    # 结束位置
    result = 0
    for i in range(start, end):
        #print(md5(i)[md5start:md5length])
        if md5(i)[0:4] == keymd5:            # 拿到加密字符串
            result = i
            print("[+]Got result:\n"+ str(result))    # 打印
            break
            


list=[]  # 参数列表
for i in range(10):   # 多线程的数字列表 开始与结尾
    list.append(str(10000000*i) + ':' + str(10000000*(i+1)))
pool = ThreadPool()    # 多线程任务
pool.map(findmd5, list) # 函数 与参数列表
pool.close()
pool.join()


