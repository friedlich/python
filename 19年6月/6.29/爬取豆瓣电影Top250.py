#这是爬取豆瓣电影Top250，并存为本地csv的代码

import requests,  random, csv
from bs4 import BeautifulSoup
csv_file=open('movieTop.csv', 'w', newline='',encoding='utf-8')
writer = csv.writer(csv_file)

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        title = titles.find('span', class_="title").text
        list1 = [title]
        writer.writerow(list1)
csv_file.close()