import requests,bs4,csv,sys
scores = dict()
film_all = []
for i in range(10):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    url = 'https://movie.douban.com/top250?start=' + str(25*i) +'&filter='
    res = requests.get(url,headers=headers)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    bsdata = soup.select('.grid_view')[0].select('li')
    for data in bsdata:
        num = data.select('em')[0].text
        title = data.select('.title')[0].text
        rating = data.select('.rating_num')[0].text
        href = data.select('a')[0]['href']
        comment = data.select('.inq')
    # soup_0=soup.find('ol',class_='grid_view')
    # lists=soup_0.find_all('li')
    # for i in lists:
    #     num=i.find('em',class_='').text[:]
    #     href=i.find('a')['href']
    #     rating=i.find('span',class_='rating_num').text
    #     title=i.find('span',class_='title').text
    #     comment=i.find('span',class_='inq')
        if comment:
            comment = comment[0].text
        else:
            comment = ''
        resa = [num,title,rating,comment,href]
        film_all.append(resa)
        scores[int(num)-1] = rating
# print(film_all)
order = sorted(scores.items(),key = lambda x:x[-1], reverse=True)
# for i in dict(order): # 知道为什么错了么，写了再擦，写了再擦，最后只留下最后一部电影的信息了
with open(sys.path[0] + '\\top250.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['序号','电影名称','评分','评语','链接'])
    for i in dict(order):
        writer.writerow(film_all[i])


    