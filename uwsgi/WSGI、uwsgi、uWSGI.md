[toc]

---

[出处](https://www.cnblogs.com/jayxuan/p/10785062.html)

# WSGI

web服务器网管接口，是一套 ==**协议**==。
用于接收用户请求并将请求进行初次封装，然后交给web框架；



# uwsgi
是一个 <u>uWSGI服务器自有的 ==**协议**==</u>，它用于定义传输信息的类型。
每一个uwsgi packet（数据信息包）前 4byte为传输信息类型描述，用于与nginx等代理服务器通信；

![出处](https://img2018.cnblogs.com/blog/1484492/201904/1484492-20190428174210592-265891904.png)


# uWSGI
uWSGI是一个 ==**web服务器**==，它实现了WSGI协议、uwsgi协议、HTTP等协议。