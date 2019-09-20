http://117.51.147.155:5050/index.html

看出来，是go写的 猜测存在整数溢出

而且买票时，票价只可以多 ，不可以少。此时可以猜到是溢出，从而实现购买。

毕竟以前做过一部分整数溢出的WEB

参考了这两个做过的题（https://www.cnblogs.com/zaqzzz/p/9984576.html）
```
9223372036854775807   // 可以输入，显示正常
9223372036854775808   // 报500，无法输入
```
以为是思路错误 又开始看ngnix中间件的整数溢出漏洞（https://www.jianshu.com/p/8602ce5faad5）

现在看来当时属实是疯了的，有病乱投医

最后看到网上的大佬的Wp才知道 还可以有抄作业这种操作

http://paper.tuisec.win/detail/537b9a69273dfbf

<img src="/contest/2019.4.12DDCTF/[WEB]大吉大利，今晚吃鸡/76b907ddf944d20a2d21fd2a7e9124dc.png">

然后就好说了 写脚本注册领券杀就ok了
