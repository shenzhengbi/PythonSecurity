from exercise.common import *
def do_reg():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    phone = input("请输入手机号码：")
    result = query_mysql(f"select username from user where username='{username}'")
    if len(result) == 0:
        update_mysql(f"insert into user(username, password, role, createtime) values('{username}', '{password}', 'user', now())")
    else:
        print("用户名已经存在，不允许注册.")

if __name__ == '__main__':
    do_reg()