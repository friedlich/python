import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
for i in range(3):
    url_list='https://www.qiushibaike.com/text/page/'+str(1+i)+'/'

    res=requests.get(url_list)
    soup=BeautifulSoup(res.text,'html.parser')
    datas=soup.find('div',id="content-left")
    for data in datas.find_all('div',class_="article"):
        name=data.find('h2').text
        comment=data.find('span').text
        print(comment)