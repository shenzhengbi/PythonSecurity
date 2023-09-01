import os

# os.system("ipconfig")       # 利用os.system执行系统指令，并输出结果

# eval("print('Hello Woniu')")    # 将字符串按照Python代码来执行
# eval("os.system('ipconfig')")

result = os.popen("ipconfig").read()
print(result)