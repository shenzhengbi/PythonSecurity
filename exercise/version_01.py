# from exercise.common import check_username, check_password, check_phone
from exercise.common import *   # 可以一口气全部引用，但是不推荐

# username = ''
# password = ''
# phone = ''

def input_username():
    # global username
    username = input("请输入用户名：")
    if check_username(username):
        print("用户名正确.")
        return username
    else:
        print("用户名错误.")
        input_username()    # 递归调用函数自身，完成循环的功能

def input_password():
    # global password
    password = input("请输入密码：")
    if check_password(password):
        print("密码正确.")
        return password
    else:
        print("密码错误.")
        input_password()

def input_phone():
    # global phone
    phone = input("请输入手机号：")
    if check_phone(phone):
        print("手机号正确.")
        return phone
    else:
        print("手机号错误.")
        input_phone()


def do_reg():
    username = input_username()
    password = input_password()
    phone = input_phone()

    user_list = []
    user = {'username': username, 'password': password, 'phone': phone}
    user_list.append(user)

    print(user_list)


if __name__ == '__main__':
    do_reg()