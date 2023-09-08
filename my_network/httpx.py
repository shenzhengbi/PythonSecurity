import requests

#发送get请求
# resp = requests.get('http://localhost/learn/php/')
#
# #resp.encoding = 'utf-8'
# print(resp.text) #获取源码

data = {'username':'szb','password':'0000','verifycode':'0000'}
resp = requests.post(url='http://localhost/learn/php/login.php',data=data)
print(resp.text)
print(resp.headers)
