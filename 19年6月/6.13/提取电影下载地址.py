import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

movie = input('你想看什么电影呀？')
gbkmovie = movie.encode('gbk')
#将汉字，用gbk格式编码，赋值给gbkmovie
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
#将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
print(url)
res = requests.get(url)
#下载××电影的搜索页面
print(res.status_code)
res.encoding ='gbk'
#定义res的编码类型为gbk
#print(res.text)
soup_movie = BeautifulSoup(res.text,'html.parser')
#print(soup_movie)
#解析网页
urlpart = soup_movie.find(class_="co_content8").find_all('table') # find('table')
print(urlpart)

if urlpart:
    urlpart = urlpart[0].find('a')['href'] # urlpart.find('a')('href')
    print(urlpart)
    urlmovie = 'https://www.ygdy8.com/' + urlpart
    print(urlmovie)
    res1 = requests.get(urlmovie)
    res1.encoding = 'gbk'
    soup_movie1 = BeautifulSoup(res1.text,'html.parser')
    urldownload = soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href'] # find('a').text
    print(urldownload)
else:
    print('没有' + movie)
    # 有些电影是查询不到没下载链接的，因此加了个判断


# import requests
# from bs4 import BeautifulSoup
# from urllib.request import quote
# #quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
# res = requests.get('https://www.ygdy8.com/')
# bs = BeautifulSoup(res.text,'html.parser')
# bs = bs.find(class_="co_content8")
# for i in bs.find_all('tr'):
#     x = i.find_all('a')
#     #print(type(x))
#     #print(len(x))
#     if len(x) == 2:
#         download = x[1]['href']
#         print(download)
#     elif len(x) == 1:
#         continue
