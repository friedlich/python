import requests
from bs4 import  BeautifulSoup

res_music = requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')
# 请求html，得到response
bs_music = BeautifulSoup(res_music.text,'html.parser')
# 解析html
list_music = bs_music.find_all('a',class_='js_song')
# 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
for music in list_music:
# 对查找的结果执行循环
    print(music['title'])