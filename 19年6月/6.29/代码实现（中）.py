# 首先是邮箱功能的代码：

import smtplib 
from email.mime.text import MIMEText
from email.header import Header
#以上，是引入相关库。

mailhost='smtp.qq.com'
qqmail = smtplib.SMTP()
qqmail.connect(mailhost,25)
#以上，皆为连接服务器。

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
qqmail.login(account,password)
#以上，皆为通过账号、密码来登录邮箱。

receiver=input('请输入收件人的邮箱：')
#以上，是获取收件人的邮箱。

content = '获取的电影链接'

message = MIMEText(content, 'plain', 'utf-8')
#content为上一个程序拿到的电影链接
subject = '电影链接'
message['Subject'] = Header(subject, 'utf-8')
#以上，是填写邮件的正文主题和正文。

try:
    qqmail.sendmail(account, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
qqmail.quit()
#以上，是发送邮件。

# 接着是定时功能的代码：  
import schedule
import time

def job():
    print("该看电影啦")

schedule.every().friday.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# #引入smtplib、MIMETex和Header

# mailhost='smtp.qq.com'
# #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
# qqmail = smtplib.SMTP()
# #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
# qqmail.connect(mailhost,25)
# #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
# #以上，皆为连接服务器。

# account = input('请输入你的邮箱：')
# #获取邮箱账号，为字符串格式
# password = input('请输入你的密码：')
# #获取邮箱密码，为字符串格式
# qqmail.login(account,password)
# #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
# #以上，皆为登录邮箱。

# receiver=input('请输入收件人的邮箱：')
# #获取收件人的邮箱。

# #content为上面的电影链接
# #输入你的邮件正文，为字符串格式
# content = '电影链接'
# message = MIMEText(content, 'plain', 'utf-8')
# #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
# subject = '电影链接'
# #输入你的邮件主题，为字符串格式
# message['Subject'] = Header(subject,'utf-8'