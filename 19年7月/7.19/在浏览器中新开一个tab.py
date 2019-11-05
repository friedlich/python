# 本文介绍如selenium方法打开一个新的tab，我们知道在浏览器里，我们按住 ctrl+ t 就可以新打开一个tab。所以我们学习如何利用webdriver
# 中send_key 的方法去触发ctrl+t的效果。我们利用火狐浏览器来演示。
# 相关代码如下：
# 主要是调用了keys模块下相关方法，可以通过这个方法，输入任何一个键盘上支持的字符或者快捷键。
# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
 
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
 
driver.get("http://www.baidu.com/")
time.sleep(1)
ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  # 触发ctrl + t
time.sleep(1)

