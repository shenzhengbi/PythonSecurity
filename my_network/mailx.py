#直接导入python内置的库
#创建连接，smtp是明文发送，base64编码，可以破译
import smtplib,time
#创建消息
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#定义发件人和收件人
sender = '864439931@qq.com'
receivers = '864439931@qq.com'

#构建邮件主体
msg = MIMEMultipart()
msg['Subject'] = 'python测试邮件'
msg['From'] = sender
msg['To'] = receivers


body = '''
<div style='font-size:30px;color:red;'>邮件的正文</div>
'''
content = MIMEText(body,'html','utf-8')
msg.attach(content)

# #建立与邮件
# smtObj = smtplib.SMTP() #如果是基于SSL，则smtplib.SMTP_SSL（）
# smtObj.connect('smtp.qq.com',587)
# smtObj.login(user=f"{sender}",password='ghgjxldcrbdrbccc')
# smtObj.sendmail(sender,receivers,str(msg))
# smtObj.quit()

#建立与邮件，加密smtp+ssl
smtObj = smtplib.SMTP_SSL('smtp.qq.com',465)

smtObj.login(user=f"{sender}",password='ghgjxldcrbdrbccc')
smtObj.sendmail(sender,receivers,str(msg))
smtObj.quit()

'''
这是chatgpt写的qq邮箱，主要看里面添加附件的部分
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 配置您的SMTP服务器和登录信息
smtp_server = 'smtp.qq.com'
smtp_port = 587  # QQ邮箱的SMTP端口号
username = 'your_email@qq.com'  # 您的QQ邮箱地址
password = 'your_password'  # 您的QQ邮箱授权码

# 创建SMTP连接
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # 启用TLS加密

# 登录到您的邮箱账户
server.login(username, password)

# 构建邮件内容
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'recipient_email@qq.com'  # 收件人的QQ邮箱地址
msg['Subject'] = '您的主题'

# 邮件正文
body = '这是一封来自Python的测试邮件。'
msg.attach(MIMEText(body, 'plain'))

# 附件（可选）
attachment_path = 'path/to/your/attachment.pdf'
with open(attachment_path, 'rb') as attachment_file:
    attachment = MIMEApplication(attachment_file.read(), Name='attachment.pdf')
attachment['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
msg.attach(attachment)

# 发送邮件
server.sendmail(username, 'recipient_email@qq.com', msg.as_string())

# 关闭SMTP连接
server.quit()
'''
