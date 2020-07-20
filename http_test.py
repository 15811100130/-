"""
http请求相应演示
"""

from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 8800
ADDR = (HOST, PORT)

sock = socket()
sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False)
rlist = [sock]
wlist = []
xlist = []
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sock:
            sock_fd, addr = r.accept()
            print("连接地址", addr)
            sock_fd.setblocking(False)
            rlist.append(sock_fd)
        else:
            data = r.recv(4096)

            print(data.decode())
            fr = open("index.html", "r")
            html = "HTTP/1.1 200 OK\r\n"
            html += "Content-Type:text/html\r\n"
            html += "\r\n"
            html += fr.read()

            r.send(html.encode())

            r.close()
