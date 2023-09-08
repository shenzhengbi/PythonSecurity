import threading ,time

#单线程的情况下，下述代码消耗5秒钟
def test_01():
    for i in range(5):
        print(time.strftime('%Y%m%d-%H%M%S'))
        time.sleep(1)

#使用多线程的方式输入5次时间
def test_02():
    print(threading.currentThread().getName()) #MainThread
    print(time.strftime('%Y%m%d-%H%M%S'))
    time.sleep(1)

#使用多线程模拟流量泛红 攻击woniusales



if __name__ == '__main__':
    #test_01() #当python执行是，虽然没有手工启动线程，默认python或启动一个主线程
    #test_02()
    for i in range(5):
        t = threading.Thread(target=test_02) #实例化一个线程，并且指定调用test_02函数
        t.start() #启动线程
        #输出结果，一秒钟结束
        # Thread-1
        # 20230907-111600
        # Thread-2
        # 20230907-111600
        # Thread-3
        # 20230907-111600
        # Thread-4
        # 20230907-111600
        # Thread-5
        # 20230907-111600