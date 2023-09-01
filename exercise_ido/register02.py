from basic import registercondition
users = [{'username': 's12345', 'password': 's321123', 'phone': '13911111090'}, {'username': 's12344', 'password': 's321123', 'phone': '13911111091'}]





while True:
    o = input("按1登录，按2注册,其余操作退出:")
    if o == '1':
        registercondition.do_sign(users)
    elif o == '2':
        registercondition.do_reg(users)
        print(users)

    else:
        break

