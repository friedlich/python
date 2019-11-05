from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.get('https://y.qq.com/')
js = " window.open('https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html')" #可以看到是打开新的标签页 不是窗口
browser.execute_script(js)
time.sleep(2)
browser.close() #关掉第一个页面
# pageSource = browser.page_source
# soup = BeautifulSoup(pageSource,'html.parser') 
# lyric = soup.find(id="lrc_content").text.replace(' ','').split()
# print(lyric)
# browser.close() #关掉第一个页面
