v4 = "2410488"
print("moctf{",end="")
for i in range(len(v4)):
    ans = ((2*ord(v4[i])-96)/4+3)%10
    print(int(ans),end="")
print("}")
