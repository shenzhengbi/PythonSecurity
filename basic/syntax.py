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

# 进制运算
#字符与ascii

print(ord("A")) #65
print(ord("强")) #2438
print(chr(65))#A
print(chr(24378))#强

#进制
print(bin(78))#0b1001110,0b标识了二进制,bin这些函数出来的是二进制字符串
print(oct(78))#0o116
print(hex(78))#0x4e

#左移右移
a = 0b00111100
print(a<<1) #左移一位相当于*2
print(a>>1)

b = 11
#print(bin(b)>>1),错误，bin（b）是字符串，不能右移操作
print(int(bin(b),2)>>1) #5

# in  not in,包括字符串，列表或元组。in	如果在指定的序列中找到值返回 True，否则返回 False。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if(a in list):
    print("a在list中")
else:
    print("a不在list中")

if(b not in list):
    print("b不在list中")
else:
    print("b在list中")

#身份运算符，身份运算符用于比较两个对象的存储单元i，	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) ,
# 如果引用的是同一个对象则返回 True，否则返回 False
#is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
#id() 函数用于获取对象内存地址。,is 与 == 区别：is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
a = [1, 2, 3]
b = a #b等于的是a的地址
print(a == b)#True
print(a is b)#True

b = a[:] #b等于的是a内部的值，所以b is not a
print(a == b) #True
print(a is b) #False

#数值转换
print(int(123.534)) #int 取整
print(round(123.534)) #round四舍五入
print(round(123.534,2)) #round四舍五入,从哪里开始四舍五入
print(float(123))
print(float("123.56"))
print(int(float("123.56")))
print(str(phone))

import random
r = random.randint(1,10) #包含1，包含10
#print(r)

r = random.randrange(1,10,2) #生成一个介于 1（包括）和 10（不包括）之间,第三个参数 2 是步长（stride）
#每次调用 random.randrange(1, 10, 2) 都可能返回 1、3、5、7 或 9 中的一个随机奇数，这取决于生成的随机数。

r = random.uniform(1.5,3.5) #取小数

r = random.choice("adadlafd")#在序列中选，列表，元组
print(r)

#字符串
soucre = 'fadhalifh'
print(soucre[1:5]) #切片操作，不包含最后一位，左闭右开
print(soucre[2:]) #2到底
print(soucre[2::2])#2到底，每隔两个取一个值，设置步长

#字符串内置方法
print(soucre.count("a")) #a在字符串中出现的次数
print(len(soucre)) #取长度

soucre = "zhangsan,lisi,wangwu"
print(soucre.split(',')) #将字符串安装，拆分为一个列表['zhangsan', 'lisi', 'wangwu']

list = soucre.split(',')
print('#'.join(list)) #合并列表，中间加#

source = "hello蜗牛2345"
target = source.encode() #encode方法将字符串按照指定类型转换为字节类型，默认utf-8
print(target) #b'hello\xe8\x9c\x97\xe7\x89\x9b2345'

soucre = b'hello\xe8\x9c\x97\xe7\x89\x9b2345'
print(soucre.decode()) #将字节类型转换为字符串，按照指定类型

print(soucre.decode('gbk')) #hello铚楃墰2345,乱码

soucre = '蜗牛学'
print(soucre.encode('gbk')) #b'\xce\xcf\xc5\xa3\xd1\xa7'
target = b'\xce\xcf\xc5\xa3\xd1\xa7'
print(target.decode('gbk'))

soucre = "\t  hello \n\t"
print(soucre)
print(soucre.strip()) #清除字符左右不可见字符



