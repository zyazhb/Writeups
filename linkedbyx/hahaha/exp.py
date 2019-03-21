import hashlib
import random
import itertools

array = [['S','s'],['1','!'],['2','@'],['E','e'],['C','c'],['H','h'],['N','n']]
sha1str="e6079c5ce56e781a50f4bf853cdb5302e0d8f054"

def gg_random():
    while True:
        temp = ""
        for i in array:
            guess = i[random.randint(0,1)]
            temp = temp+str(guess)
        flag = "flag{"+  temp +"}"
        #print("\n[-]Trying： " + flag +"\n")
        #print("\n[-]sha1: " + hashlib.sha1(flag.encode('utf8')).hexdigest())
        #print(sha1str)

        if(hashlib.sha1(flag.encode('utf8')).hexdigest()==sha1str):
              print("\n[+]Found:"+flag)
              break
def right_answer():
    temp = list("a"*7)
    for a in array[0]:
        temp[0]=a
        for b in array[1]:
            temp[1]=b
            for c in array[2]:
                temp[2]=c
                for d in array[3]:
                    temp[3]=d
                    for e in array[4]:
                        temp[4]=e
                        for f in array[5]:
                            temp[5]=f
                            for g in array[6]:
                                temp[6]=g
                                for g in itertools.permutations(temp,7):
                                    flag = "flag{"+  "".join(g) +"}"
                                    if(hashlib.sha1(flag.encode('utf8')).hexdigest()==sha1str):
                                        print("\n[+]Found:"+flag)
                                        flag="sh@1enc"
                                        print("\n[+]md5=" + hashlib.md5(flag.encode('utf8')).hexdigest())
                                        break
right_answer()
        
