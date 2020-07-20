"""
selcet的并发
"""
from socket import *
from select import select
import time

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8880))
tcp_sock.listen(5)

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(("0.0.0.0", 8800))

f = open("msg.log", "rb")

# 开始监控这些IO
# print("监控IO发生")
print("监控IO发生")
time.sleep(5)
rs, ws, xs = select([tcp_sock, udp_sock], [f, udp_sock], [])
print("rs:", rs)
print("rs:", ws)
print("rs:", xs)

# sock = socket(AF_INET, SOCK_STREAM)
# sock.bind(("0.0.0.0", 8800))
# sock.listen(5)
# # 设置套接字的非阻塞
# # sock.setblocking(False)
# # 设置套接字仅阻塞三秒
# # sock.settimeout(3)
# while True:
#     fa = open("msg.log", "a")
#     print("等待连接....")
#     try:
#         sock_fk, addr = sock.accept()
#         print(addr, "已连接")
#     except (BlockingIOError, timeout) as e:
#         msg = "%s:%s\n" % (time.ctime(), e)
#         fa.write(msg)
#         # time.sleep(2)
#         fa.close()
#     else:
#         data = sock_fk.recv(1024)
#         print(data.decode())
