#无参无返回
import random


def test_01():
    print("这个函数没有返回值和参数")

test_01()


#有参无返回
def test_02(a,b):
    result = a+b
    print(f"{result}")

test_02(1,2)

#有参有返回
def test_03(a,b):
    result = a+b
    return  result

print(test_03(1,2))

def test_04():
    print("test_04")

x = test_04
print(x) #<function test_04 at 0x0000013D962B7EE0>
x()
print("===========")
def test_05(func):
    func()
    print("test_05")

print(test_05(test_01))
#这个函数没有返回值和参数
#test_05
#None
print("===============")
print(type(test_04)) #<class 'function'>
print(type(random.choice)) #<class 'method'>
print(hex(id("hello"))) #0x263d36461b0

print("=================================================")
'''
python 里面的参数
1,必需参数
2，默认值参数
3，可变长参数，可选参数,加*说明*args,
4，字典参数，在可变长参数后还可以定义字典参数，加**说明**kwargs
'''

def test_args_01(a,b,c=11):
    result = a+b+c
    print(result)

test_args_01(1,2)
test_args_01(1,2,3)
test_args_01(c=11,a=1,b=6) #这种情况不用关注位置,在传参时，直接指定参数名称
print("===============")

def test_args_02(a,b,c=11,d=344,*args):
    result = a+b+c+d
    print(result)
    print(args) #可变长参数，是以元组的形式存在
    print(*args) #加上*，展开，将元组展开

test_args_02(12,43)
#410 #()
test_args_02(12,23,45,23) #45,23给了默认参数，没有给变长参数*args
test_args_02(12,23,45,23,7) #7给了*args
#print(args) 打印的是（7，）
#print(*args) 打印的是7
print("===========")
def test_args_03(a,b,c=10,d=12,*args,**kwargs):
    result = a+b+c+d
    print(result)
    print(args)
    print(kwargs)

test_args_03(1,2,3,4,56,67) #(56, 67)都给了可变长参数*args
test_args_03(1,2,3,4,5,6,name="xiaoxiao",age="22")
'''(5, 6)
{'name': 'xiaoxiao', 'age': '22'}
'''


#1,2， 3,4的参数顺序不要乱
#如果将函数交给其他用户调用，为了应对复杂情况，参数不确定等，可以用可变参数和字典参数



