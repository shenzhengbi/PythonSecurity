#当导入一个模块的时候，相当于将模块直接执行了一遍
#定义模块级变量，和函数或者类同级
source = "模块级变量"
def test_01():
    global  source #使用global才能使用模块级的变量，不加就代表新声明了一个变量
    source = "change"
    print("这个函数没有返回值和参数")
#有参无返回
def test_02(a,b):
    result = a+b
    print(f"{result}")

#有参有返回
def test_03(a,b):
    result = a+b
    return  result

def test_04(func):
    print(func.__name__)


print(__name__) #在当前模块打印__name__魔术变量时，值为__main__
#为了防止别的模块在导入模块时，重复执行以下代码
#其本质是判断下面代码是在当前模块执行，还是在其他文件被调用执行，其他文件import 模块时，会执行一遍import的文件。
if __name__=='__main__':
    test_01()
    test_04(test_02)