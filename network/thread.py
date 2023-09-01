# 并发操作：如果一个单核的CPU，是不存在严格意义的并发，只是因为处理时间极短，所以感觉上是并发操作的。
# 针对多核CPU，4核CPU，严格意义上的并发处理是4个

# 线程和进程
# 1、每一个应用程序，至少会有一个进程，并且拥有PID和独立的内存空间。
# 2、每一个进程，至少拥有一个线程，而线程并没有独立的内存空间。

import threading, time, requests, random

# 单线程情况下，下述代码执行或消耗5秒钟的时间
def test_01():
    print(threading.currentThread().getName())  # 输出当前线程的名字
    for i in range(5):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

# 使用多线程的方式输入5次时间
def test_02():
    # print(threading.currentThread().getName())
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)


# 使用多线程模拟流量泛洪（FLow Flood）-攻击WoniuSales
# 定义一个装饰器，可以用于收集其响应时间
def performance(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f"请求：{func.__name__} 的响应时间为：{round(end - start, 4)}")
    return inner

session = requests.session()

@performance
def home():
    resp = session.get('http://192.168.112.130:8080/woniusales/')
    if '成都蜗牛创想科技有限公司' in resp.text:
        print('首页访问成功.')
    else:
        print('首页访问失败.')

@performance
def login():
    data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
    resp = session.post(url='http://192.168.112.130:8080/woniusales/user/login', data=data)
    if resp.text == 'login-pass':
        print('登录系统成功.')
    else:
        print('登录系统失败.')

@performance
def add():
    data = {'customername':'未和','customerphone':f'13{random.randint(300000000, 999999999)}','childsex':'男','childdate':'2021-10-15','creditkids':'0','creditcloth':'0'}
    resp = session.post('http://192.168.112.130:8080/woniusales/customer/add', data=data)
    if resp.text == 'add-successful':
        print('新增会员成功.')
    else:
        print('新增会员失败.')

# 基于HTTP协议，进行流量泛洪，压力测试，性能测试
def woniusales_flood():
    for i in range(1000):
        home()
        login()
        add()


if __name__ == '__main__':
    # test_01()   # 当Python执行时，虽然没有手工启动线程，默认Python或启动一个主线程。

    # for i in range(5):
    #     t = threading.Thread(target=test_02)    # 实例化一个线程，并且指定调用test_02函数
    #     t.start()                               # 启动线程

    for i in range(500):
        threading.Thread(target=woniusales_flood).start()