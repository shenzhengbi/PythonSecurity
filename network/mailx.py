# 直接导入内置模块
import smtplib, time    # smtplib模块主要用于处理SMTP协议
# email模块主要处理邮件的头和正文等数据
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 定义发件人和收件人
sender = 'student@woniuxy.com'  # 发送邮箱
receiver = 'dengqiang@woniuxy.com'  # 接收邮箱

# 构建邮件的主体对象
msg = MIMEMultipart()
msg['Subject'] = 'Python测试邮件'
msg['From'] = sender
msg['To'] = receiver

body = '''
<div style='font-size: 30px; color: red;'>这是一个邮件的正文, 
<a href='http://www.woniuxy.com'>点我有惊喜</a></div>
'''
content = MIMEText(body, 'html', 'utf-8')
msg.attach(content)

# 添加邮件附件
attachment = MIMEApplication(open('D:/test.jpg', 'rb').read())
filename = 'test.jpg'
attachment.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(attachment)

# 建立与邮件服务器的连接并发送邮件
smtpObj = smtplib.SMTP()   # 如果基于SSL，则 smtplib.SMTP_SSL
smtpObj.connect('mail.woniuxy.com', '25')
smtpObj.login(user='student@woniuxy.com', password='Student123')
smtpObj.sendmail(sender, receiver, str(msg))
smtpObj.quit()

# 如果登录SMTP+SSL邮件服务器（QQ服务器不支持连续不停止发送），如果要发送多封，建议第一款之间sleep几秒种
smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtpObj.login(user='15903523@qq.com', password='XXXXXXX')
smtpObj.sendmail(sender, receiver, str(msg))
smtpObj.quit()
