# 针对数据库的操作，一共分三步：
# 1、建立数据库连接
# 2、执行SQL语句
# 3、关闭数据库连接

# Python操作数据库（如：MySQL），Python发送能够与数据库直接通信的数据包，并获取数据库服务器的响应结果。
# 是一种典型的基于TCP/IP的通信过程，要求必须要满足数据库服务器的数据包规则。
# 在Python中，要操作MySQL，需要依赖于第三方库：pymysql，先安装：pip install pymysql

import pymysql

# # 建立连接
# conn = pymysql.connect(host='192.168.112.188', user='qiang', password='123456', database='learn', charset='utf8')
#
# # 操作数据库
# # 先定义一个游标对象(默认情况下，游标对象返回的结果是元组
# cursor = conn.cursor()
# # 执行SQL语句
# sql = "select username,password,role from user where userid<6"
# cursor.execute(sql)
# # 获取结果集
# result = cursor.fetchall()
#
# for row in result:
#     print(row[0], row[1], row[2])
#
# # 关闭连接
# conn.close()


from pymysql.cursors import DictCursor
# 将游标对象定义为 字典 类型，进而通过 列表+字典 的格式获取结果集
# conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
# cursor = conn.cursor(DictCursor)
# sql = "select username,password,role from user where userid<6"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# for row in result:
#     print(row['username'])
# conn.close()


# 更新操作，比如修改某个用户的信息
# 更新的操作，必须确认提交，两种方式：一种是设置autocommit为True，另外则是在代码中显式提交
# conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8', autocommit=True)
cursor = conn.cursor()
sql = "update user set password='123456789' where userid=13"
cursor.execute(sql)
# conn.commit()   # 显式提交更新操作
conn.close()