#!/usr/bin/python
from pwn import *

Io=remote('2018shell1.picoctf.com',33158)

Io.sendline('cd secret')
Io.sendline('ls')
Io.sendline('rm intel*')
Io.sendline('cd ..')
Io.sendline('cd executables')
Io.sendline('ls')
Io.sendline('./dontLookHere')
Io.sendline('whoami')
Io.sendline('cp /tmp/TopSecret passwords')
Io.sendline('cd ..')
Io.sendline('cd passwords')
Io.sendline('cat TopSecret')
#Io.recvuntil('$')
Io.interactive()
Io.close()
