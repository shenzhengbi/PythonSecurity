from exercise.common import *   # 可以一口气全部引用，但是不推荐

def input_username():
    username = input("请输入用户名：")
    if check_username(username):
        if check_user_exists(username):
            print("用户名已存在.")
            return input_username()
        else:
            print("用户名正确.")
            return username
    else:
        print("用户名错误.")
        return input_username()    # 递归调用函数自身，完成循环的功能

def input_password():
    password = input("请输入密码：")
    if check_password(password):
        print("密码正确.")
        return password
    else:
        print("密码错误.")
        return input_password()

def input_phone():
    phone = input("请输入手机号：")
    if check_phone(phone):
        print("手机号正确.")
        return phone
    else:
        print("手机号错误.")
        return input_phone()

def do_reg():
    username = input_username()
    password = input_password()
    phone = input_phone()

    with open('./userpass.csv', mode='a') as f:
        f.write(f"\n{username},{password},{phone}")
        print("恭喜你，注册成功.")

    draw_menu()

def do_login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    user = check_get_user(username)
    if user is None:
        print("用户名不存在.")
        exit(0)
    elif user['password'] == password:
        print("用户名密码正确，登录成功.")
    else:
        print("登录失败.")

    draw_menu()

def do_change():
    username = input("请输入用户名：")
    password = input("请输入旧密码：")
    user = check_get_user(username)
    if user is None:
        print("用户名不存在.")
        draw_menu()
    elif user['password'] == password:
        newpass = input("请输入新密码：")
        change_password(username, newpass)
    else:
        print("旧密码验证不通过.")

def draw_menu():
    print("========= 欢迎使用用户管理系统 ===========")
    print("1、注册   2、登录   3、修改密码   4、退出")
    option = input("请选择菜单项：[1 2 3 4]：")
    if option == '1':
        do_reg()
    elif option == '2':
        do_login()
    elif option == '3':
        do_change()
    elif option == '4':
        exit(0)
    else:
        print("请输入正确的菜单编号.")
        draw_menu()

if __name__ == '__main__':
    # do_reg()
    # do_login()
    do_change()
    # draw_menu()