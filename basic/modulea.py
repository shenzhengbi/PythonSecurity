# import moduleb
# moduleb.test()

# 定义模块级变量（直接隶属于当前模块，与函数或类同级，可以被其他函数直接引用）
source = "模块级变量"
list = [11,22,33,44,55]

def test_01():
    print("这是一个没有参数没有返回值的函数")
    global source   # 使用global声明为全局变量后，才可以正确引用到模块级的全局变量
    source = "Hello Module - Variable"
    # global list
    # list = [1,2,3]
    list.append(66)


def test_02(a, b):
    result = a+b
    print(result)

def test_03(a, b):
    result = a+b
    return result

def test_04(func):
    print(func.__name__)

# test_01()

# 当在当前模块中打印__name__魔术变量时，其值为 __main__ (字符串）
# 如果在其他模块中引用当前模块，则打印的__name__为当前模块的真实模块名称，而非 __main__
# print(__name__)

# 为了防止别的模块在导入时重复执行以下代码，必须添加一个判断条件：
# 其本质就是判断当前代码是否在当前模块中直接运行，还是在其他模块中被导入时运行的
if __name__ == '__main__':
    test_01()
    test_04(test_02)


class A:
    pass
