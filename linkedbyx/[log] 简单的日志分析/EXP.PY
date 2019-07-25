import re
import datetime
lasttime = datetime.datetime.strptime("00:00:00",'%H:%M:%S')
lasti = "9:46:51"
lastc="0"
file = open('file')
for i in file:
    time = re.findall("[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}",i)
    time = str(time)[7:-2]
    time = datetime.datetime.strptime(time,'%H:%M:%S')
    #print (time-lasttime)
    c = str(re.findall("\('[0-za-z%D]{1,}'\)",i))[4:-4]
    if str(time - lasttime) == "0:00:00" or str(time - lasttime) == "0:00:01":
        count = re.findall("1\),[0-9]{1,2}",i)
        #print (str(count) +str(time - lasttime)+ " is: " +lastc,end="\n")
        print(lastc,end="")
        #print(i)
    lasttime = time
    lastc = c
'''
28 4 38 g
1234567890 1234567890 1234567890 1234567
flag{50f1ea7cf1544106e3555c4cc2cf4087g}
50f1ea7cf1544106e3555c4cc2cf4087g
'''
