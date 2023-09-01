import pymysql
from pymysql.cursors import DictCursor

class DB:
    def __init__(self, host='localhost', user='root', password='123456', database='learn', charset='utf8', type='default'):
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
        self.cursor = None
        if type == 'default':
            self.cursor = self.conn.cursor()
        elif type == 'dict':
            self.cursor = self.conn.cursor(DictCursor)
        else:
            raise Exception("参数type的值不正确，只能为：default或dict.")

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('执行更新操作成功.')
        except:
            print('执行更新操作出现异常，请确认.')

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    db = DB(type='dict')
    print(db.query('select * from user'))