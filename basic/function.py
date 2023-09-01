# Python中的函数和参数的用法
# 函数的构成：
# 1、函数名（必须有，且在同一作用范围中不允许重复）
# 2、参数（可以没有），遵守标准的命名规范
# 3、返回值（可以没有），如果没有返回值，则返回为None

# 无参数，无返回值
def test_01():
    print("这是一个没有参数没有返回值的函数")

# 有参数，无返回值
def test_02(a, b):
    result = a+b
    print(result)

# 有参数，有返回值
def test_03(a, b):
    result = a+b
    return result

# 直接将函数名进行赋值或输出
def test_04(func):
    func()
    print("Hello")

# test_01()
# test_02(100,200)
# r = test_03(100, 200)
# print(r)

# 直接将函数名进行赋值或输出
# x = test_04
# print(type(x))
# x(test_01)
# test_04(test_01)

# source ="hello"
# print(type(source))
# print(hex(id(source)))
#
# import random
# random.choice('ABCDEFG')
#
# list = [1,2,3]
# print(list)
# print(type(list))


'''
Python里面的参数分为以下4种：
1、必需参数（位置参数：positional argument）
2、默认值参数（定义形参时，可以设置一个默认值）
3、可变长参数，可选参数，必须加 * 号说明
4、字典参数，关键字参数，在可变长参数之后，还可以定义字典参数，必须加 ** 声明
参数的顺序：1、2、3、4，不能乱
'''
def test_args_01(a, b, c=100):
    result = a * b + c
    print(result)

# test_args_01(5, 10)
# test_args_01(5, 10, 200)
# test_args_01(c=5, a=10, b=200)      # 在传参时，直接指定参数名称，可以不用关注参数的位置（推荐该用法）

def test_args_02(a, b, c=100, d=200, *args):
    result = a * b + c * d
    print(result)
    print(args)     # 可变长参数，是以元组的形式存在
    print(*args)    # 在元组或列表前加 *，表示将该数据展开

# test_args_02(10, 50, 5, 6)
# test_args_02(10, 50, 5, 6, 7, 8, 9)

def test_args_03(a, b, c=100, d=200, *args, **kwargs):
    result = a * b + c * d
    print(result)
    print(args)
    print(kwargs)

test_args_03(10, 50, 5, 6, 7, 8, 9, name='zhangsan', age=30)
test_args_03(10, 50, 5, 6, 7, 8, 9, name='zhangsan', age=30)    #
# test_args_03(10, 50, 5, 6, 7, 8, 9, name='zhangsan', age=30, a=100)     # 字典参数不能包含位置参数或默认值参数

# 通常情况下，自定义函数，并且不需要交由第三方调用时，或者不考虑各类复杂场景时，位置参数和默认值参数足够。
# 如果需要将函数交由其他用户调用，或开发的是一套框架，需要考虑各种复杂调用情况，或者参数不确定，则加可变参数和字典参数。

test_01()