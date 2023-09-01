# 异常处理

# 在连接到MySQL数据库的过程中，如果不有效地处理异常，则异常信息过于复杂，对于用户太不友好，暴露过多敏感信息
# 所以，在真实的生产环境中，程序必须有效地处理和控制异常，按照既定的流程进行

import pymysql

# 最基础的异常处理结构：try ... except ....
# try:
#     conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
#     print("连接到数据库成功.")
# except:
#     print("连接到数据库失败.")

# 更完整的异常处理结构：try ... except ... finally ...
# try:
#     conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("select * from users")
#     print("连接到数据库成功.")
# except:
#     print("连接到数据库失败.")
# finally:
#     conn.close()
#     print("无论成功与否，本代码都会执行，数据库连接关闭.")


# 针对不同的异常，展示不同的错误信息
# try:
#     conn = pymysql.connect(host='localhost', user='root', password='1234567', database='learn', charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("select * from user")
#     a = 1/0
# except pymysql.err.OperationalError as e:
#     # print(e)
#     print("数据库连接不正确.")
# except pymysql.err.ProgrammingError as e:
#     print("SQL语句不正确.")
# except ZeroDivisionError as e:
#     print("除数不能为零.")
# except Exception as e:
#     print("代码还存在其他异常.")
# finally:
#     # conn.close()
#     pass

# pymysql.err.OperationalError
# pymysql.err.ProgrammingError


# from exercise.common import query_mysql_2
# try:
#     result = query_mysql_2("select * from users where userid < 6")
#     print(result)
# except:
#     pass





# JSON的处理
# import json
# from exercise.common import query_mysql
#
# row_list = query_mysql("select username, password, role from user where userid < 6")
# print(row_list)
# print(type(row_list))
#
# # 将Python对象序列化成字符串
# jsonstr = json.dumps(row_list)
# print(jsonstr)
# print(type(jsonstr))
#
# # 将JSON字符串反序列化成Python对象
# source = '[{"username": "woniu", "password": "123456", "role": "editor"}, ' \
#          '{"username": "qiang", "password": "654321", "role": "editor"}]'
# jsonobj = json.loads(source)
# print(jsonobj[1]['username'])
#
# # json库还有 json.load和json.dump，用于操作文件
# with open("./jsonstring.txt", mode='w') as f:
#     json.dump(row_list, f)





# 装饰器：在函数或方法或类前面，使用 @ 符号进行声明的特殊操作，可以改变程序的执行顺序
# 统计某段代码的执行时间
import time

def test():
    start = time.time()
    result = 9999
    for i in range(30000):
        result = result + i - result * 15
    end = time.time()
    print(end - start)

# test()


# 定义装饰器，用于统计函数的运行时间
# 函数里面继续定义了一个函数，则之为内部函数（闭包）
# 装饰器自带一个参数，func，用于获取被装饰函数的地址
# 内部函数运行结束后，必须要返回其函数名（地址）
def stat(func):
    def inner():
        start = time.time()
        func()      # 调用被装饰的函数
        end = time.time()
        print(end - start)
    return inner

@stat
def test2():
    result = 9999
    for i in range(30000):
        result = result + i - result * 15
    print(result)

test2()

# @stat
# def haha():
#     result = 9999
#     for i in range(30000):
#         result = result + i - result * 15
#     # print(result)




list = [53,80,443,21,109,110,995,143,993,25,69,23,123,68,67,546,22,161,1863,465,119,563,389,636,3269,50389,50636,137,138,139,520,162,9988,5355,7,135,79,8080,1494,1723,1701,445,1433,1755,1812,1813,3389,520,513,135,554,5060,5061,1080,3544,43,9988]
list.sort()
print(list)

# 常见端口
list = [7, 21, 22, 23, 25, 43, 53, 67, 68, 69, 79, 80, 81, 88, 109, 110, 113, 119, 123, 135, 135, 137, 138, 139, 143, 161, 162, 179, 194, 220, 389, 443, 445, 465, 513, 520, 520, 546, 547, 554, 563, 631, 636, 991, 993, 995, 1080, 1194, 1433, 1434, 1494, 1521, 1701, 1723, 1755, 1812, 1813, 1863, 3269, 3306, 3307, 3389, 3544, 4369, 5060, 5061, 5355, 5432, 5671, 5672, 6379, 7001, 8080, 8081, 8088, 8443, 8883, 8888, 9443, 9988, 9988, 15672, 50389, 50636, 61613, 61614]
print(list)