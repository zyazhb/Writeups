import hashlib

str1='access denieda'
str2=''
flag=''

for i in range(len(str1)):
    str2 += chr(ord(str1[i]) ^ i )
for i in range(len(str1)):
    if i%3 == 0:
        flag += chr(ord(str2[i]) ^ 31)
    elif i%3 == 1:
            flag += chr(ord(str2[i]) ^ 32)
    else:
            flag += chr(ord(str2[i]) ^ 33)

print(flag)

print(hashlib.md5(flag.encode('utf8')).hexdigest())
