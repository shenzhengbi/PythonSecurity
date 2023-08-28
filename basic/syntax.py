# a=1
# a=1.2
# a=-3
# a=[1,2,3]
# a=['张三','李四']
# a={'name':'张三','age':'12'}
# a=(1,2,5)
student={'name':'张三','age':'12'}
print(student['age'])

string = "这是电话号码"
#phone1 = input("输入电话号码：") 命令行输入
phone = 1381119082
#print(string+phone).这样要转换格式
print(string,phone)
print(string + str(phone))
print('%s%d'%(string,phone))
print(f"{string}{phone}")
print("{}{}".format(string,phone))

point = 1234.3223
print("%.2f"%point)
print("{:.2f}".format(point))