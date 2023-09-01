import socket

# 定义一个客户端连接
def test_client():
    # 建立与服务器的连接
    s = socket.socket()     # 此类实例的方式，默认使用TCP协议
    s.connect(('192.168.112.130', 554))

    # 传输数据（收发数据包）
    content = "Welcome to Woniu College"
    s.send(content.encode('gbk'))

    # 关闭连接
    s.close()

# test_client()

# 定义一个服务器端
def test_server():
    s = socket.socket()
    s.bind(('192.168.112.1', 555))  # 绑定服务器端IP和端口号
    s.listen()                      # 保持对555端口的监听
    while True:
        chanel, client = s.accept()     # 接收来自客户端的数据
        message = chanel.recv(1024)
        print(message.decode())

# test_server()