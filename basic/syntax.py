# a=200
# b=123.45
# c=-123
# a="Hello"
# a=[1,2,3,4,5,6]
# b=['张三', '李四', '王五', '赵六']

# student = {'name':'张三', 'age': 25, 'sex':'男', 'phone': '13812345678'}
# print(student['phone'])

# string1 = "Hello\nWorld"
# string2 = '你好蜗牛'
# print(string1, end='\n')
# print(string2)

# string = '这是我的电话号码：'
# phone = input("请输入电话号码：")
# phone = 13812345678
# print(string + str(phone))
# print('%s%d' % (string, phone))
# print(f"{string}{phone}")
# print("{}{}".format(string, phone))
#
# point = 12345.6789
# print("%.2f" % point)
# print("{:.2f}".format(point))
#
# str="Hello"
# print(str*5)
#
# student = {'name':'张三', 'age': 25, 'sex':'男', 'phone': '13812345678'}
# print(student.get('phone'))
# student['sex']='女'
# print(student.keys())

# 关于进制与字符转换的运算
# 字符与ASCII码的转换
# print(ord("A"))     # 65
# print(ord("强"))    # 24378
# print(chr(65))      # A
# print(chr(24378))   # 强

# 进制转换
# print(bin(78))     # 0b1001110
# print(oct(78))     # 0o116
# print(hex(78))     # 0x4e
#
# a = 0b00111100
# b = 0b00001101
# print(bin(a&b))         # 0b00001100

# 左移，1100 (12)  << 1  11000 (24)
# a = 0b111100
# a = 100
# print(a<<1)         # a=60，左移1位，相当于*2，左移2位，*4
# print(a>>1)         # a=60，右移1位，相当于/2


# 数值的类型转换
# print(int(123.456))
# print(int(123.556))
# print(int(-123.556))
# print(round(123.556, 2))
# print(float(12345))
# print(float("123.45"))
# print(int(float("123.45")))
# phone = 13812345678
# print("电话号码是：" + str(phone))

# 数值类型

# 随机数
# import random   # 导入一个模块
# r1 = random.randint(1, 10)   # 生成一个闭区间的随机数
# print(r1)
# r2 = random.randrange(1, 10)    # 左闭右开
# r2 = random.randrange(1, 10, 2)    # 设置步长，只从1、3、5、7、9范围内生成随机数
# print(r2)
# r3 = random.uniform(1.5, 3.5)   # 指定范围内的随机小数
# print(r3)
# r4 = random.choice("ABCDEFGHIJK")   # 序列化数据类型
# print(r4)
# r5 = random.choice([1,2,3,4,5,6,7,8,9])
# print(r5)


# 字符串切片操作
# source = 'HelloWoniu'
# # print(source[2])        # 取下标
# # print(source[0:5])      # 字符串切片操作，左闭右开
# # print(source[1:])       # 从第2个开始到最后
# # print(source[:5])       # 从最开始到第5个位置前
# # print(source[-1])       # 取最后一个
# # print(source[1:-2])     # 从第2个取到倒数第2个之前
# # print(source[0:5:2])    # 设置步长为2
#
# # 字符串内置方法
# print(source.count('l'))   # 子字符串在字符串中出现的次数
# print(len(source))         # 取字符串长度
#
# source = "zhang,li,wang,zhao,zhou"
# print(source.split(','))
# list = ['zhang', 'li', 'wang', 'zhao', 'zhou']
# print('#'.join(list))
#
# # source = "HelloWoniu12345"
# source = "Hello蜗牛学院12345"
# print(source.encode())    # encode方法将字符串按照指定的编码格式转换成字节类型，默认编码格式为UTF-8
#
# source = b'\xe8\x9c\x97\xe7\x89\x9b\xe5\xad\xa6\xe9\x99\xa2'
# print(source.decode())   # 将字节类型按照指定的编码格式转换成字符串，默认编码格式为UTF-8
#
# source = '蜗牛学院'
# print(source.encode('gbk'))
# source = b'\xce\xcf\xc5\xa3\xd1\xa7\xd4\xba'
# print(source.decode('gbk'))
#
# source = '  \t Hello \n \t   '
# print(source.strip())       # 清除字符串左右的不可见字符


# def tuple_usage():
#     # a, b, c = 1,2,3
#     a, b, c = [11,22,33]
#     a, b, c = (11,22,33)
#     print(a)
#
#     return a,b      # 在Python中，函数可以返回元组类型
#
# c, d = tuple_usage()
# print(d)


import random
names = ['王庆　','沙华　','代亚伟','罗浩然','许光升','李佳霖','罗先　','邱月　','刘琪　',
         '封婉萍','章瀚玺','刘佳丽','代畅　','郑宇　','李炳菊','陈洁　','秦妍　','马鑫连',
         '王小林','李健　','魏仕界','郑敏　','尹萍　','杨瑞　','王佳伟']
print(random.choice(names))
