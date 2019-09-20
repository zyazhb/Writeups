#!/usr/bin/python
from pwn import *

Io=remote('104.154.106.182',7777)

Io.sendline('CRACKME02')
Io.sendline(p64(0xDEADBEEF))
Io.sendline('ZXytUb9fl78evgJy3KJN')
Io.sendline('1')
#Io.sendline()
#Io.recvuntil('$')
Io.interactive()
Io.close()
