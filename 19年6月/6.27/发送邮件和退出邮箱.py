import smtplib 
#smtplib是python的一个内置库，所以不需要用pip安装
mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以SMTP对象的方法和属性了
qqmail.connect(mailhost,25)
#连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
#以上，皆为连接服务器的代码

account = input('请输入你的邮箱：')
#获取邮箱账号
password = input('请输入你的密码：')
#获取邮箱密码
qqmail.login(account,password)
#登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码    

receiver=input('请输入收件人的邮箱：')
#获取收件人的邮箱

from email.mime.text import MIMEText
from email.header import Header
#引入Header和MIMEText模块
content=input('请输入邮件正文：')
#输入你的邮件正文
message = MIMEText(content, 'plain', 'utf-8')
#实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码.
subject = input('请输入你的邮件主题：')
#用input()获取邮件主题  
message['Subject'] = Header(subject, 'utf-8')
#在等号的右边，是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。

qqmail.sendmail(account, receiver, message.as_string())
#发送邮件，调用了sendmail()方法，写入三个参数，分别是发件人，收件人，和字符串格式的正文。
qqmail.quit()
#退出邮箱
