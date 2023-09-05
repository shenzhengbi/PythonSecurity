import re, pymysql
from pymysql.cursors import DictCursor

'''
长度的判断5-12位，使用len函数进行判断
不能以数字开头：username[0]不能是0-9的范围
如何判断只能是大小写或数字：
返回值：True: 用户名正确， False: 用户名错误
'''
def check_username(username):
    if len(username) < 5 or len(username) > 12:
        return False

    if username[0] >= '0' and username[0] <= '9':
    # if not (username[0] < '0' or username[0] > '9'):
        return False

    for char in username:
        if not (ord(char) in range(65, 91) or ord(char) in range(97, 123) or ord(char) in range (48, 58)):
            return False

    return True


'''
检查密码：由大写、小写和数字构成，且必须是6~15位
只要确保密码中至少有1位是大写，至少有1位是小写，至少有1位是数字
'''
def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    lower = 0
    upper = 0
    digit = 0
    other = 0

    for char in password:
        if char >= 'A' and char <= 'Z':
            upper += 1
        elif char >= 'a' and char <= 'z':
            lower += 1
        elif char >= '0' and char <= '9':
            digit += 1
        else:
            other += 1

    if upper < 1 or lower < 1 or digit < 1 or other > 0:
        return False

    return True

# 检查电话号码
def check_phone(phone):
    pattern = "^1[3-9]\d{9}$"
    if re.match(pattern, phone):
        return True
    else:
        return False



# 读取CSV，并动态将第一行处理为字典的Key，返回[{},{}]的格式
def read_csv(csvfile, has_column=True):
    with open(csvfile) as f:
        line_list = f.readlines()

    if not has_column:
        raise Exception('CSV文件必须要使用第一行作为列名')
        # return None

    key_list = line_list[0].strip().split(',')

    list = []
    for i in range(1, len(line_list)):
        temp_list = line_list[i].strip().split(',')

        dict = {}
        for j in range(len(temp_list)):
            dict[key_list[j]] = temp_list[j]

        list.append(dict)

    return list


# 读取csv文件，并检查用户名是否存在
def check_user_exists(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if user['username'] == username:
            return True

    return False

# 根据用户名取得CSV文件中对应的一行用户数据，以字典的形式返回
def check_get_user(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if user['username'] == username:
            return user

    return None


# 修改用户的密码，修改一个CSV文件中的某一行中的某一列，不能直接修改（Python中不存在文件内容部分修改的操作）
# 将CSV整体读入到内存中，形成列表+字典，然后修改字典的某一项，再整体写入到CSV（覆盖写入）
def change_password(username, newpass):
    csv_list = read_csv('./userpass.csv')
    for user in csv_list:
        if user['username'] == username:
            index = csv_list.index(user)
            break
    csv_list[index]['password'] = newpass
    # 将列表+字典还原成行+逗号分隔数据
    with open('./userpass.csv', mode='w') as f:
        f.write("username,password,phone\n")
        for user in csv_list:
            line = f"{user['username']},{user['password']},{user['phone']}\n"
            # print(line)
            # line = line.replace("'","")
            f.write(line)


# 针对数据库连接进行封装操作
def query_mysql(sql):
    #conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
    conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8')
    cursor = conn.cursor(DictCursor)
    cursor.execute(sql)
    result =cursor.fetchall()
    conn.close()
    return result

def update_mysql(sql):
    #conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
    conn = pymysql.connect(host='192.168.72.136',user='root',password='0908',database='woniusales',charset='utf8')
    cursor = conn.cursor(DictCursor)
    cursor.execute(sql)
    conn.commit()
    conn.close()

# 利用异常处理改造查询函数
def query_mysql_2(sql):
    try:
        conn = pymysql.connect(host='localhost', user='root', password='123456', database='learn', charset='utf8')
        cursor = conn.cursor(DictCursor)
        cursor.execute(sql)
        result =cursor.fetchall()
        return result
    except:
        # print("数据库处理出错.")
        raise Exception("数据库处理出错.")     # 主动抛出异常，让程序停止
        # pass
    finally:
        conn.close()



# 最基本最简单的单元测试代码：半自动化测试代码
# print(check_username('qiang'))
# print(check_username('132457'))
# print(check_username('Q132457'))

# 全自动的单元测试代码，编写一个测试驱动程序
def test_driver(func, expect, *args):
    actual = func(*args)
    if actual == expect:
        print("测试 %s: 成功" % func.__name__)
    else:
        print("测试 %s: 失败" % func.__name__)

if __name__ == '__main__':
    pass
    # 测试用户名的规则
    # test_driver(check_username, False, 'hi')
    # test_driver(check_username, False, 'welcomeToWoniu123')
    # test_driver(check_username, True, 'qiang')
    # test_driver(check_username, False, '132457')
    # test_driver(check_username, True, 'Q132457abc')
    # test_driver(check_username, False, 'Q13#@%$bc')

    # 测试密码的规则，TDD：Test-Driven Development
    # test_driver(check_password, False, 'qiang')
    # test_driver(check_password, False, 'welcomeToWoniu1231235')
    # test_driver(check_password, False, 'WELCOME')
    # test_driver(check_password, False, '12349234')
    # test_driver(check_password, False, 'jojojoju1')
    # test_driver(check_password, False, 'WILL12432')
    # test_driver(check_password, True, 'Woniu123')
    # test_driver(check_password, False, 'Woniu@#123')

    # test_driver(check_phone, False, '1881234567')
    # test_driver(check_phone, False, '188123456799')
    # test_driver(check_phone, False, '988123456799')
    # test_driver(check_phone, False, '128123456799')
    # test_driver(check_phone, True, '13812345679')
