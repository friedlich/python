import requests
from bs4 import BeautifulSoup
import smtplib
import schedule,time
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱账号：')
password = input('请输入你的邮箱授权码：')
receiver = input('请输入收件人邮箱账号：')

def recipe():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,URL,ingredients])
    # print(list_all)
    return list_all

def send_mail(list_all):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content = list_all
    message = MIMEText(content,'plain','utf-8')
    subject = '这周的菜谱'
    message['Subject'] = Header(subject,'utf-8')
    try:
        send_mail(account,receiver,message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()
def job():
    print('第一次尝试：')
    list_all = recipe()
    send_mail(list_all)
    print('任务完成')
schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

