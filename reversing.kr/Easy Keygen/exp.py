Serial = "5B134977135E7D13"
Name = ''
a = [16, 32, 48]
for i in range(len(Serial)//2):
    Name += chr(int(Serial[2*i:2*i+2], 16) ^ a[i%3])
print(Name)
