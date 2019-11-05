import smtplib 
#smtplib是python的一个内置库，所以不需要用pip安装
mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以使用SMTP对象的方法和属性了
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
