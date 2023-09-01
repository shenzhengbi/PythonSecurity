# 面向对象的核心特点：
# 1、类与实例：类有属性和方法，实例用于调用
# 2、封装：可以决定哪些属性和方法是可以访问的（public），哪些是受保护的（protected），哪些是私有的（private)
# 3、继承：子类继承父类所有可访问的方法和属性
# 4、多态：通常只有强类型编程语言（C#，C++，Java）才严格具备多态性，弱类型编程语言本身就体现为多态

# 类名建议大驼峰规则：所有首字母大写，缩写词全部大写， StudyPython
class People:
    # 定义类属性
    course = '网络安全'

    # name = ''
    # age = 0
    # nation = ''
    # addr = ''

    # 定义构造方法：实例化时会自动调用的方法，并且可以将实例变量（实例属性）定义于此
    # self形参：类实例的引用，与其他语言当中的 this 关键字类似，必须是类方法的第一个形参
    # 且建议使用self，但是可以 自定义名称
    def __init__(self, name='张三', age=30, nation='汉族', addr='成都高新区'):
        # 定义实例变量
        self.name = name
        self.age = age
        self.nation = nation
        self.addr = addr
        print("构造方法正在调用")

    # 析构方法：用于释放内存空间时使用
    def __del__(self):
        print("实例空间正在被释放")

    # 当打印类的实例时会触发的方法
    def __str__(self):
        return f'当前类的实例正在被打印，其内存地址为{hex(id(self))}'

    # 定义受保护的方法
    def _test01(self):
        print("受保护方法")

    # 定义私有方法
    def __test02(self):
        print("私有方法")

    # 定义类方法
    def talk(self):
        # print("People正在说话.")
        print(f"{self.name}正在说话.")

    def work(self, type):
        print(f"People正在做{type}的工作.")

    # 静态方法：直接使用类名而非实例调用的方法，静态方法常驻类的内存空间
    @classmethod
    def teach(cls):         # cls代表对类本身的引用
        print(cls.course)   # 类属性course用类的引用cls来调用


# 新建一个类：Man，继承至People
class Man(People):
    # 重写父类的talk方法
    def talk(self):
        print('子类正在说话')

    # 子类扩展自己的新方法
    def drive(self):
        print("子类可以开车")


if __name__ == '__main__':
    # 基本的类的实例化及调用
    p1 = People()   # 类的实例化
    p2 = People()
    print(id(People))
    print(id(p1))
    print(id(p2))

    p1.name = '张三'
    p2.name = '李四'
    print(p1.name)
    print(p2.name)
    p1.talk()
    p2.work(type='编程')


    # 通过构造方法进行实例化
    p = People()
    p = People('张三',30,'汉族','成都高新区')
    p = People(addr='上海浦东新区')
    print(p.name)
    print(p.addr)

    p.teach()           # 类的静态方法，不建议使用实例进行调用
    People.teach()      # 类的静态方法，直接使用类名调用

    print(p)


    # 子类Man的操作
    m = Man()
    m.talk()
    m._test01()
    # m.__test02()    # 子类无法直接调用受保护的方法



from basic.db import DB

db = DB()
result = db.query('select username, password from user where userid < 5')
print(result)