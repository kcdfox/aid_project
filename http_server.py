"""
搭建一个http服务，当浏览器发起请求的时候向浏览器发送 index.html 网页

* 将sadsa4
"""

"""
http基本演示
"""
from socket import *


def requst():
    # http请求
    data = c.recv(2048)
    # 防止客户端退出，data=空
    if not data:
        return
    info = data.decode().split(' ')[1]
    print("请求内容：", info)
    if info == '/':
        #将网页给客户端
        f = open('index.html')
        # 发送数据给浏览器
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += f.read()
    else:
        data = "HTTP/1.1 404 Not Found\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += "Sorry.."

    c.send(data.encode())  # 发送响应内容
    c.close()


# 创建套接字
s = socket()
s.bind(('127.0.0.1', 8100))
s.listen(3)

# 等待客户端（浏览器）链接
while True:
    c, addr = s.accept()
    print("Connect from", addr)
    requst()  # 调用请求处理函数

s.close()
