import time
import paramiko

# transport = paramiko.Transport(('192.168.112.188', 22))
# transport.connect(username='root', password='123456')
#
# ssh = paramiko.SSHClient()
# ssh._transport = transport
# sftp = paramiko.SFTPClient.from_transport(transport)

# 执行命令并获取命令的结果
# stdin, stdout, stderr = ssh.exec_command('ls /opt')
# stdin, stdout, stderr = ssh.exec_command('ip addr')
# stdin, stdout, stderr = ssh.exec_command('sh /opt/learn/pingall.sh')
# print(stdout.read().decode())

# 传输文件
# sftp.put('./test.jpg', '/opt/test.jpg')
# sftp.get('/opt/woniusales-centos7.9.tar.gz', './woniusales.tar.gz')

# import requests
#
# resp = requests.get('http://192.168.112.188:8080/woniusales')
# if resp.status_code >= 400:
#     ssh.exec_command('/opt/apache-tomcat-8.0.47/bin/shutdown.sh')
#     time.sleep(3)
#     ssh.exec_command('/opt/apache-tomcat-8.0.47/bin/start.sh')
#     time.sleep(20)
# resp = requests.get('')





# import socket
#
# s = socket.socket()
# s.connect(('192.168.112.188', 6379))
# s.send('*2\r\n$4\r\nauth\r\n$6\r\n123456\r\n'.encode())
# print(s.recv(1024).decode())
# # time.sleep(1)
# s.send('*3\r\n$3\r\nset\r\n$4\r\nname\r\n$7\r\nwoniuxy\r\n'.encode())
# print(s.recv(1024).decode())
# # time.sleep(1)
# s.send('*2\r\n$3\r\nget\r\n$4\r\nname\r\n'.encode())
# print(s.recv(1024).decode())


import redis

red = redis.Redis(host='192.168.112.188', port=6379, password='123456', db=0)
red.set('addr', 'chengdu')
print(red.get('addr').decode())
red.rpush('students', 'zhangsan')
red.rpush('students', 'lisi')
red.rpush('students', 'wangwu')
print(red.lindex('students', 1))