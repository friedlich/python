# 这是爬电影的下载链接的代码

import requests
from bs4 import BeautifulSoup
from urllib.request import quote

movie=input('你想看什么电影？')
gbkmovie = movie.encode('gbk')
urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
res = requests.get(urlsearch)
res.encoding='gbk'
# soup_movie = Beaut