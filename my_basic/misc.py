import pymysql

#最基础try except
# try:
#     conn = pymysql.connect(host='192.168.72.136',user='root',password='09081',database='woniusales',charset='utf8')
#     print("连接到数据库")
# except:
#     print("数据库连接失败")

#try except finally，finally无论有没有异常，都会执行
# try:
#     conn = pymysql.connect(host='192.168.72.136',user='root',password='09081',database='woniusales',charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("select creditid,userid,category from credit where creditid<3")
#     print("连接到数据库")
# except:
#     print("数据库连接失败")
# finally:
#     conn.close()
#     print('无论成功与否，都会执行')



#异常信息
#pymysql.err.OperationalError
#pymysql.err.ProgrammingError
#
# try:
#
#     conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("select creditid,userid,category from credit where creditid<3")
#     a = 1 / 0
#     print("连接到数据库")
# except pymysql.err.OperationalError as e:
#     print("数据库连接失败")
# except pymysql.err.ProgrammingError as e:
#     print("语法错误")
# except Exception as e:
#     print("代码还有其他异常")
# finally:
#     #conn.close()
#     print('无论成功与否，都会执行')


#json处理
import json
from exercise.common import query_mysql
row_list = query_mysql("select creditid,userid,category from credit where creditid<3")
print(row_list)
print(type(row_list))#<class 'list'>

#将python对象序列化为字符串
jsonstr = json.dumps(row_list)
print(jsonstr)
print(type(jsonstr))#<class 'str'>


#将json对象反序列化为python对象
source = '[{"creditid": 1, "userid": 5, "category": "\u6dfb\u52a0\u8bc4\u8bba"}, {"creditid": 2, "userid": 5, "category": "\u6b63\u5e38\u767b\u5f55"}]'
jsonobj = json.loads(source)
print(jsonobj[1]['category'])

#json库中load和dump用来操作文件
#将python对象，以json格式写入文件
# with open("./jsonstring.txt",mode='w') as f:
#     json.dump(row_list,f)

#将json格式文件读取为python对象
# with open("./jsonstring.txt",mode='r') as f:
#     print(type(json.load(f)))


#装饰器，在函数或者方法或者类的前面加上@进行声明操作，可以改变程序的执行顺序
#统计某段代码的执行时间
import time


#定义装饰器，用于统计函数的运行时间
#装饰器自带func用来获取被装饰函数的地址，内部函数运行结束后要返回器地址
def stat(func):
    def inner():
        start = time.time()
        func() #被装饰的函数是在这里被调用。
        end = time.time()
        print(end- start)
    return inner

@stat
def test():

    result = 9999
    for i in range(30000):
        result = result+i-result*15
    print(result)


@stat
def test1():

    result = 99999
    for i in range(30000):
        result = result+i-result*15
    print(result)


#调用函数test（），发现其被stat装饰，这时他会将test函数地址传给stat，执行stat装饰函数
#函数test（），会在调用装饰函数stat中的func位置调用test。
test()
test1()