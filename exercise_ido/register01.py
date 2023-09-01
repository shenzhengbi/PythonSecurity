from basic import registercondition
users = [{'username':'s12345'}]

#输入用户名，并且判断是否合法，是否存在
def input_username():
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
    return phone

def do_reg():
    username = input_username()
    password = input_password()
    phone = input_phone()
    user = {'username':username,'password':password,'phone':phone}
    users.append(user)


if __name__ == '__main__':
    do_reg()