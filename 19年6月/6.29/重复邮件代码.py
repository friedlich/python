import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入发件人的邮箱账号：')
password = input('请输入发件人的邮箱授权码：')
receiver = input('请输入收件人的邮箱账号：')

def weather():
    url = 'http://www.weather.com.cn/weather1d/101020100.shtml'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.encoding='utf-8'
    bsdata = BeautifulSoup(res.text,'html.parser')
    wea1 = bsdata.find(class_="wea")
    tem1 = bsdata.find(class_="tem")
    wea = wea1.text
    tem = tem1.text
    return wea,tem

def send_mail(wea,tem):
    global account,password,receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP_SSL()
    qqmail.connect(mailhost,465)
    qqmail.login(account,password) 
    content = '亲爱的，今天的天气是：'+tem+wea
    message = MIMEText(content,'plain','utf-8')
    subject = '天气预报'
    message['Subject'] = Header(subject,'utf-8')
    try:
        qqmail.sendmail(account,receiver,message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

def job():
    print('开始第一次任务')
    wea,tem = weather()
    send_mail(wea,tem)
    print('任务完成')

schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)







