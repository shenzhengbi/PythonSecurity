import socket

#下面是单工通信，只收不发，只发不收

#定义一个客户端连接,只发不收  (代码流程，连接发送)
def test_client():
    s = socket.socket() #此类实例的方式默认tcp协议
    s.connect(('192.168.72.128',554))


    #传输数据（收发数据包
    content = "welcom to szb channel欢迎来到"
    s.send(content.encode('gbk'))

    #关闭连接
    s.close()

#建立一个服务器端，只收不发   （代码流程，绑定监听接收）
def test_sever():
    s = socket.socket()

    #绑定服务器和端口并且监听
    s.bind(('192.168.72.1',554))#绑定服务器端口
    s.listen()  #保持对554端口的监听


    while True: #一直监听
        chanel,client = s.accept() #接受来自客户端的数据
        message = chanel.recv(1024)#收取字节
        print(message.decode())#转字节编码
test_sever()


