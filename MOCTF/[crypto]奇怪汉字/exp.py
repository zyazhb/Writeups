'''
当铺密码，汉字有多少个出头就是几
102 117 110 110 121
'''
import codecs
string = "102 117 110 110 121"
string = string.split(" ")
for i in string:
    print(chr(int(i)),end="")
