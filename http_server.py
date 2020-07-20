"""
思考问题:
1.使用流程
2.那些量需要用户决定,怎么传入
 2.1哪组网页
 2.2服务器地址
"""
import re
from socket import *
from select import *


class WebServer:
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 做IO多路复用并发模型准备
        self.__rlist = []
        self.__wlist = []
        self.__xlist = []
        self.cerate_socket()
        self.bind()

    def cerate_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def start(self):
        self.sock.listen(10)
        print("等待连接....%d" % self.port)
        self.__rlist.append(self.sock)
        while True:
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__xlist)
            for r in rs:
                if r is self.sock:
                    sock_fd, addr = self.sock.accept()
                    sock_fd.setblocking(False)
                    self.__rlist.append(sock_fd)
                else:
                    try:
                        self.handle(r)
                    except:
                        self.__rlist.remove(r)
                        r.close()

    def handle(self, sock_fd):
        reqeust = sock_fd.recv(1024 * 10).decode()
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, reqeust)
        if result:
            info = result.group('info')
            # 发送响应内容
            self.send_response(sock_fd, info)

        else:
            self.__rlist.remove(sock_fd)
            sock_fd.close()

    def send_response(self, sock_fd, info):
        if info == '/':
            file_name = self.html + "/index.html"
        else:
            file_name = self.html + info
        try:
            fr = open(file_name, "rb")
        except:
            html = "HTTP/1.1 404 OK\r\n"
            html += "Content-Type:text/html\r\n"
            html += "\r\n"
            html += "<h1>Sorry....</h1>"
            html = html.encode()
        else:
            data = fr.read()
            html = "HTTP/1.1 200 OK\r\n"
            html += "Content-Type:text/html\r\n"
            html += "Content-Length:%d\r\n" % len(data)
            html += "\r\n"
            html = html.encode() + data
        finally:
            sock_fd.send(html)


if __name__ == '__main__':
    httpd = WebServer(host='0.0.0.0', port=8800, html="/home/tarena/lbx/two/day17/static")
    httpd.start()


# def main():
#     pass
