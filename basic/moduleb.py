# 另外在导包时，注意不要循环导入，在A中导入B，在B中导入A
# import modulea
# modulea.test_01()

def test():
    print("Hello Module")

test()

# import function     # 当导入一个模块的时候，事实上是将该模块的源代码直接执行了一遍

# 导入到模块级，调用时，用 模块.函数 的方式进行调用
# import modulea
# modulea.test_01()
# print(modulea.source)
# print(modulea.list)
#
# import random
# random.choice([1,2,3,4])

# 通过from...import...导入到函数级，那么直接在代码中调用函数即可
# from modulea import test_01
# test_01()
#
# from random import choice
# print(choice([1,2,3,4,5]))

# 通常情况下，在同一个包下，可以不需要在 导入 时明确声明包名，但是，建议无论在何种情况下，把包名加上
# 直接使用 import 只能到 模块级，不能到函数或类级
# import basic.modulea
# basic.modulea.test_01()
#
# from basic import modulea
# modulea.test_01()

# 如果要直接导入到函数或类级，则必须使用 from ... import ...
# from basic.modulea import test_01
# test_01()

# from basic.second.demo import name