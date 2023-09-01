import requests

# 发送GET请求
resp = requests.get('http://localhost:8080/woniusales/')
resp.encoding = 'utf-8'     # 设置编码格式
print(resp.text)            # 打印响应正文

# 发送POST请求
data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
resp = requests.post(url='http://localhost:8080/woniusales/user/login', data=data)
print(resp.text)
print(resp.headers)         # 打印响应头
if resp.text == 'login-pass':       # 对响应进行判断
    print("登录成功")
else:
    print("登录失败")

# 登录成功后获取响应的Cookie，用于在后续请求中使用
cookie = resp.cookies

# 下载图片
resp = requests.get('http://www.woniunote.com/img/banner-1.jpg')
with open('./banner.jpg', mode='wb') as file:
    file.write(resp.content)

# 文件上传
file = {'batchfile': open('E:/Other/SaleList-20171020-Test.xls', 'rb')}
data = {'batchname': 'GB20211009'}
resp = requests.post(url='http://localhost:8080/woniusales/goods/upload', data=data, files=file, cookies=cookie)
print(resp.text)


# 第二种维持Session的用法（推荐）
session = requests.session()
data = {'username':'admin', 'password':'admin123', 'verifycode':'0000'}
resp = session.post(url='http://localhost:8080/woniusales/user/login', data=data)

file = {'batchfile': open('E:/Other/SaleList-20171020-Test.xls', 'rb')}
data = {'batchname': 'GB20211007'}
resp = session.post(url='http://localhost:8080/woniusales/goods/upload', data=data, files=file)
print(resp.text)
print(type(resp.text))

# 利用Python直接处理JSON
import json
list = json.loads(resp.text)    # 将字符串反序列化成List+Dict的Python对象
print(list)
print(type(list))
print(list[1]['goodsname'])     # 输出字典的某个值


# 处理HTTPS请求
resp = requests.get('https://www.woniuxy.cn', verify=False)     # 忽略证书
print(resp.text)
