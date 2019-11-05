import requests
from bs4 import BeautifulSoup
import openpyxl
import csv
import re
csv_file=open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.30/jokes.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(csv_file)
list2=['网友昵称','搞笑内容']
writer.writerow(list2)
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'jokes'
# # sheet['A1'] = '网友昵称'
# sheet['A1'] = '搞笑内容'


headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
for i in range(2):
    url_list='https://www.qiushibaike.com/text/page/'+str(1+i)+'/'

    res=requests.get(url_list,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    datas=soup.find('div',id="content-left")
    for data in datas.find_all('div',class_="article"):
        name=data.find('h2').text.strip().replace('"','')
        name=re.sub('"','',name)
        comment=data.find('span').text.strip()
        comment=re.sub('",','',comment)
        list1 = [name,comment]
        # print(name,comment)
        writer.writerow(list1)
        # sheet.append([comment])
# wb.save(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.30/jokes1.xlsx')
csv_file.close()