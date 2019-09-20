import hashlib

md5_1 = "31f40dc5308fa2a311d2e2ba8955df6c"

array_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
#array_2 = "0123456789"

for i in range(len(array_1)):
    a = array_1[i]
    for j in range(len(array_1)):
        b = array_1[j]
        for k in range(len(array_1)):
            c = array_1[k]
            for l in range(len(array_1)):
                d = array_1[l]
                for m in range(len(array_1)):
                    e = array_1[m]

                    flag = "tjctf{" + a + b + c + d + e + "}"
                    #print(md5_2)
                    md5_2 = hashlib.md5(flag.encode('utf-8')).hexdigest()
                    #print(md5_2)
                    if md5_2 == md5_1:
                        print(flag)
                        break
                
