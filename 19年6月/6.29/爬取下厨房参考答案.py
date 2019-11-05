import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def recipe_spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = ''
    num=0
    for food in list_foods:
        num=num+1
        tag_a = food.find('a')
        name = tag_a.text.strip()
        url = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text.strip()
        food_info = '''
        序号: %s
        菜名: %s
        链接: %s
        原料: %s
        '''%(num,name,url,ingredients)
        list_all=list_all+food_info
    return(list_all)

def send_email(list_all):
    global account,password,receiver
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP_SSL()
    qqmail.connect(mailhost,465)
    qqmail.login(account,password)
    content= '亲爱的，本周的热门菜谱如下'+list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '周末吃个啥'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    list_all = recipe_spider()
    send_email(list_all)
    print('任务完成')

# schedule.every().friday.at("18:00").do(job)#部署每周三的13：15执行函数的任务
schedule.every(0.1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
