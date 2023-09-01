import time

import requests

# resp = requests.get('http://192.168.112.188:8080/woniusales/vcode')
# with open('./vcode.png', mode='wb') as file:
#     file.write(resp.content)
#
# resp = requests.post('./打码平台/upload', file='vcode.png')
# vcode = resp.text
#
# resp = requests.post('login', 'vcode')
#
#


session = requests.session()

resp = session.get('http://www.woniunote.com:8080/jfinalcode/vcode')
with open('./vcode.png', mode='wb') as file:
    file.write(resp.content)

time.sleep(2)

resp = session.get('http://www.woniunote.com:8080/jfinalcode/text')
print(resp.text)


# 训练