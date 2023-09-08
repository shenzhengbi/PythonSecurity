import os
#os.system("netstat -ant") #利用os.system执行系统命令，并输出结果
eval("print('hello')") #eval的作用，将里面的字符串当成代码执行
#eval("os.system('netstat -ant')")

result = os.popen("ipconfig").read() #这种方式也会执行里面的命令，不会直接输出，会放在变量里面
print(result)