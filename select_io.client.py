"""
selcet的并发
"""
from socket import *
import time

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 发起连接(服务器IP)
tcp_socket.connect(("127.0.0.1", 8880))
# 收发消息
while True:
    #    info = input("请输入消息>>")
    #    if not info:
    #        break
    tcp_socket.send("info".encode())
    # data = tcp_socket.recv(1024)
    # print("From server:", data.decode())

# tcp_socket.close()
