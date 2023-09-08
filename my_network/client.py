import socket
s = socket.socket()
#s.connect(('127.0.0.1',6666))
s.connect(('192.168.72.128',6666))

while True:
    message = input("请输入消息：")
    s.send(message.encode())
    receive = s.recv(102400)
    print(f"服务器回复：{receive.decode()}")

