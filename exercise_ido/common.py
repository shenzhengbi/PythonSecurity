import re
import sys

def phoneJudgment(phone):
    pattern = r'^1\d{10}$'
    judgment = re.match(pattern,phone) is not None
    return judgment

def userNameJudgment(username):
    if len(username)<5 or len(username)>12:
        return False
    if username[0].isdigit():
        return False
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern,username) is None:
        return False
    return True

def passwordJudgment(password):
    pattern = r'^[a-zA-Z0-9]{6,15}$'
    if re.match(pattern,password) is None:
        return False
    return True


#自动化测试
def test_driver(func,expect,*args):
    actual = func(*args)
    if actual == expect:
        print('测试%s成功'%func.__name__)
    else:
        print("测试%s失败"%func.__name__)

from basic import registercondition
users = [{'username':'s12345'}]

#输入用户名，并且判断是否合法，是否存在
def input_username(users):
    while True:
        tag = 0 #等于0表示用户名没有重复
        username = input("请输入用户名：")
        if registercondition.userNameJudgment(username) is True:
            if len(users) == 0:
                print("用户名正确")
                break
            else:
                for user in users:
                    if user['username'] == username:
                        print("用户名已经存在")
                        tag = 1
                        break
                if tag == 1:
                    continue
                else:
                    break
        else:
            print("用户名不合法，用户名只能由大小写字母和数字构成，且不能以数字开头，长度在5-12位")
            o = input("退出注册作按e，其他操作将继续输入用户名：")
            if o == 'e':
                sys.exit()
    return username


#输入密码，判断合法性
def input_password():
    while True:
        password = input("请输入密码：")
        if registercondition.passwordJudgment(password):
            print("密码合法")
            break
        else:
            print("只能包含大小写字母和数字，密码长度6-15位")
            o = input("退出注册作按e，其他操作将继续输入密码：")
            if o == 'e':
                sys.exit()
    return password


#手机号码验证
def input_phone():
    while True:
        phone = input("请输入手机号码：")
        if registercondition.phoneJudgment(phone):
            print("手机号码合法")
            break
        else:
            print("手机号不合法")
            o = input("退出手机号验证作按e，其他操作将继续输入手机号：")
            if o == 'e':
                sys.exit()
    return phone

#读取csv文件，并判断用户名是否存在
def check_user_exists(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if user['username'] == username:
            return True
    return False

def check_get_user(username):
    user_list = read_csv('./userpass.csv')
    for user in user_list:
        if user['username'] == username:
            return user
    return

#注册主流程
def do_reg(users):
    username = input_username(users)
    password = input_password()
    phone = input_phone()
    user = {'username':username,'password':password,'phone':phone}
    users.append(user)


#登录操作使用============================================================
def sign_name(users):
    username = input("请输入你的用户名：")

    for user in users:
        if user['username'] == username:
            return user
            break
    return False

def verifyPassword(user):
    for i in range(0,3):
        pw = input("输入密码：")
        if pw == user['password']:
            return True
        elif i<=3:
            print("密码错误")
            continue
        else:
            return False

def do_sign(users):
    while True:
        user = sign_name(users)
        if user == False:
            print("你的用户名不存在")
            o = input("按e退出，其他操作继续登录:")
            if o == "e":
                sys.exit()
        else:

            break

    if verifyPassword(user):
        print("密码正确，登录成功")
        succeedSign(user,users)
        sys.exit()
    else:
        sys.exit()

def changePassword(user,users):
    while True:
        np = input("输入新密码：")
        if passwordJudgment(np):
            for i in range(0, len(users)):
                if user['username'] == users[i]['username']:
                    users[i]['password'] == np
                    return True
        else:
            print("密码不合法，密码只能包含大小写字母和数字，密码长度6-15位")
            o = input("退出修改密码操作按e，其他操作将继续修改密码")
            if o=='e':
                return False

def changePhone(user,users):
    while True:
        np = input("输入新号码：")
        if phoneJudgment(np):
            for i in range(0, len(users)):
                if user['username'] == users[i]['username']:
                    users[i]['phone'] == np
                    return True
        else:

            o = input("电话不合法，退出修改密码操作按e，其他操作将继续修改密码:")
            if o=='e':
                return False

#成功登录后，可以改密码改电话
def succeedSign(user,users):
    while True:
        o = input("改密码按1，改电话按2,其余操作退出：")
        if o=='1':
           if changePassword(user,users):
               print("密码修改成功")
           else:
               print("密码修改失败")
        elif o=='2':
            if changePhone(user,users):
                print("电话修改成功")
            else:
                print("电话修改失败")
        else:
            sys.exit()



#有列名，返回[{},{},{}],无列名，返回[[],[],[]]
def read_csv(csvfile,has_column=True):

    with open(csvfile) as f:
        line_list = f.readlines()
    #print(line_list)

    if has_column:
        key_list = line_list[0].strip().split(',')
        #print(key_list)

        list = []
        for i in range(1, len(line_list)):
            temp_list = line_list[i].strip().split(',')
            dict = {}
            for j in range(len(temp_list)):
                dict[key_list[j]] = temp_list[j]

            list.append(dict)

        return list

    else:
        list=[]
        for line in line_list:
            temp_list = line.strip().split(',')
            list.append(temp_list)

        return list





if __name__ == '__main__':
    users = [{'username': 's12345', 'password': 's321123', 'phone': '13911111090'}, {'username': 's12344', 'password': 's321123', 'phone': '13911111091'}]
    do_sign(users)
     #test_driver(userNameJudgment,True,'qiang')
    # test_driver(userNameJudgment,False,'1234567')
    # test_driver(userNameJudgment,True,'Q1234567')