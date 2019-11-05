import requests,csv,random
from bs4 import BeautifulSoup
from urllib.request import quote
# 按照标准， URL 只允许一部分 ASCII 字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。
# 所以 URL 中使用其他字符就需要进行 URL 编码。
# 以上，为引入相应的库。
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
csv_file=open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\6.29\movieTop.csv', 'w', newline='',encoding='utf-8')
writer = csv.writer(csv_file)
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url,headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        title = titles.find('span', class_="title").text
        list1 = [title]
        # print(list1)
        writer.writerow(list1)
csv_file.close()
# 以上，为爬取豆瓣电影Top250的榜单，并存储为本地的csv文件。

movielist=[]
csv_file=open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\6.29\movieTop.csv',newline='',encoding='utf-8')
reader=csv.reader(csv_file)
for row in reader:
    movielist.append(row[0])
# 以上，为读取豆瓣电影Top250榜单的csv文件，并写入列表movielist中。
three_movies=random.sample(movielist,3)
print(three_movies)
# 以上，是从列表movielist中，随机抽取三部电影，取出来的是一个列表。
for movie in three_movies:
    # 以上，是把电影名从列表中取出来，并把其数据类型变为字符串。下面开始，就是你熟悉的下载电影链接的代码了。
    gbkmovie = movie.encode('gbk')
    print(gbkmovie)
    urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
    print(quote(gbkmovie))
    print(urlsearch)
    res = requests.get(urlsearch)
    res.encoding='gbk'
    soup_movie = BeautifulSoup(res.text,'html.parser')
    urlpart=soup_movie.find(class_="co_content8").find_all('table')
    if urlpart:
        urlpart=urlpart[0].find('a')['href']
        urlmovie='https://www.ygdy8.com/'+urlpart
        res1=requests.get(urlmovie)
        res1.encoding='gbk'
        soup_movie1=BeautifulSoup(res1.text,'html.parser')
        urldownload=soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href']
        content=movie+'\n'+urldownload
        print(content)
    else:
        content='没有'+movie+'的下载链接'
        print(content)