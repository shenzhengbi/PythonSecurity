import time

import paramiko
import requests

#建立ssh连接
# transport = paramiko.Transport(('192.168.72.140',22))
# transport.connect(username='root',password='0908')
#
# ssh = paramiko.SSHClient()
# ssh._transport = transport
# sftp = paramiko.SFTPClient.from_transport(transport)


#执行命令并且获取结果
#stdin, stdout, stderr = ssh.exec_command('ls /opt')
# stdin, stdout, stderr = ssh.exec_command('free')
# stdin, stdout, stderr = ssh.exec_command('top -n 1 > /opt/top.out')
# stdin, stdout, stderr = ssh.exec_command('cat /opt/top.out')
#print(stdout.read().decode())

#传输文件
#sftp.put('D:\program\Python\stduy\PythonSecurity\my_network\woniunote\image\\20230907_091812banner-1.jpg','/opt/python.jpg')
#sftp.get('/opt/tomocat.keystore.old','./tomocat.keystore.old') 下载文件

#可以和requests结合
# resp = requests.get('http://192.168.140:8080/woniusales')
# if resp.status_code > 400:
#     ssh.exec_command('/opt/tomcat/bin/shutdown.sh')
#     time.sleep(3)
#     ssh.exec_command('/opt/tomcat/bin/start.sh')
#     time.sleep(20)

# sftp.close()
# ssh.close()
# transport.close()

#建立redis连接

#搞清楚redis数据包格式，可以用socket来进行发送包，但是太麻烦，直接调用包
# import socket
# s = socket.socket()
# s.connect(('192.168.72.140',6379))
# s.send('*2\r\n$4\r\nauth*4\r\n0908\r\n'.encode())
# print(s.recv(1024).decode())
# time.sleep(1)
# s.send('*3\r\n$3\r\nset\r\n$4\r\nname\r\n$7\r\nwoniuxy\r\n'.encode())
# print(s.recv(1024).decode())
# time.sleep(1)
# s.send('*2\r\n$3\r\nget\r\n$4\r\nname\r\n'.encode())
# print(s.recv(1024).decode())
#
# s.close()

#直接调用包
import redis
red = redis.Redis(host='192.168.72.140',port=6379,password='0908',db=0)
red.set('addr','nanjing')
print(red.get('addr').decode())
red.rpush('students', 'zhangsan')
red.rpush('students', 'lisi')
red.rpush('students', 'wangwu')
print(red.lindex('students', 1))

red.close()