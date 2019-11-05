from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

# driver.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6') # 访问页面
# time.sleep(2)

# pageSource = driver.page_source
# soup = BeautifulSoup(pageSource,'html.parser') 
# bsdata = soup.select_one('.songlist__list').select('li')
# for data in bsdata:
#     music_id = data.get('mid')
#     print(music_id)
#     name = data.select_one('.songlist__songname_txt' ).text
#     print(name)
#     album = data.select_one('.songlist__album').text
#     print(album)
#     time = data.select_one('.songlist__time').text
#     print(time)
#     # href= data.select_one('a[.js_song]').get('href')
#     href= data.select_one('a[class="js_song"]').get('href')
#     # href = data.select('.songlist__songname_txt')[0].find('a')['href']
#     # href = data.select_one('.songlist__songname_txt a').get('href')
#     # href = data.find(class_="songlist__songname_txt").find('a')['href']
#     print(href)
     

# js = " window.open('https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html')" #可以看到是打开新的标签页 不是窗口
# driver.execute_script(js)
driver.get('https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html') # 访问页面
time.sleep(2)
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,'html.parser') 
lyric = soup.find(id="lrc_content").text.replace(' ','').split()
print(lyric)
driver.close()




