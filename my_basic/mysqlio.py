import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8')

#操作数据库，先定义一个游标对象
cursor = conn.cursor()

#执行sql语句
sql = "select creditid,userid,category from credit where creditid<6"
cursor.execute(sql)

#获取结果集
result = cursor.fetchall()
#以二维元组返回  ((1, 5, '添加评论'), (2, 5, '正常登录'), (3, 5, '添加评论'), (4, 1, '正常登录'), (5, 5, '正常登录'))
print(result)

conn.close()


#将游标对象定义为字典类型，进而通过列表+字典的格式获取结果集
conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8')
cursor = conn.cursor(DictCursor)
sql = "select creditid,userid,category from credit where creditid<3"
cursor.execute(sql)
result = cursor.fetchall()
#[{'creditid': 1, 'userid': 5, 'category': '添加评论'}, {'creditid': 2, 'userid': 5, 'category': '正常登录'}]
print(result)

#更新操作,必须设置提交，两种方式，一种是设置autocommit为true，另外是在代码中显示提交
conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8',autocommit=True)
cursor = conn.cursor()
sql = "update credit set createtime='2020-02-17 16:18:32' where creditid=1"
cursor.execute(sql)

conn.commit()#更新操作,必须设置提交，两种方式，一种是设置autocommit为true，另外是在代码中显示提交

conn.close()


