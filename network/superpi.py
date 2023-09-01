import os
import time
from decimal import Decimal
from decimal import getcontext
import threading, multiprocessing

def cal_pi(precision):
    getcontext().prec=precision
    result = sum(1/Decimal(16)**k *
                 (Decimal(4)/(8*k+1) -
                  Decimal(2)/(8*k+4) -
                  Decimal(1)/(8*k+5) -
                  Decimal(1)/(8*k+6)) for k in range (precision))
    print(result)

if __name__ == '__main__':
    # result = os.popen('tasklist | findstr python.exe').read()
    # list = result.split('Console')
    # print(list)
    # if len(list) < 3:

    # 如果程序已经启动，则不再启动，否则继续启动
    result = os.popen('tasklist | find /i /c "python.exe"').read()
    if int(result) < 2:
        for i in range(8):
            # threading.Thread(target=cal_pi, args=(5000,)).start()
            multiprocessing.Process(target=cal_pi, args=(5000,)).start()

    # schtasks /create /tn minerunner /tr E:\Workspace\pythonworkspace\PythonSecurity08\start_mining.bat /sc minute /mo 1