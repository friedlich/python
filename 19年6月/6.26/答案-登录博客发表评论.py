# 特别提示：
# 从博客首页进入文章页面时，需要用到 find_element_by_partial_link_text 通过链接的部分文本获取超链接。  
# 发表评论之后，不会再终端返回运行结果，记得去博客文章的页面去看看自己的评论有没有成功~  
# 由于教学系统中与你本地的浏览器设置方法不同，我给你提供了两份答案，一份可以在课程系统中运行，一份可以在你的本地运行。 

# 下面是只能在爬虫课系统中运行的答案：
from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器

driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php') # 访问页面
time.sleep(1) # 暂停两秒，等待浏览器缓冲

username = driver.find_element_by_id('user_login') # 定位到输入用户名的位置
username.send_keys('spiderman') # 输入用户名
password = driver.find_element_by_id('user_pass') # 定位到输入密码的位置
password.send_keys('crawler334566') # 输入密码
login = driver.find_element_by_id('wp-submit') # 定位到登录按钮的位置
login.click() # 点击登录
time.sleep(2) # 等待两秒

article = driver.find_element_by_partial_link_text('三') # 根据链接的部分文字"三"，定位到这个链接
article.click() # 点击链接
time.sleep(1) # 等待一秒
comment = driver.find_element_by_id('comment') # 定位到评论区
comment.send_keys('蜘蛛侠的selenium评论') # 输入评论内容，随意发挥你的创意，记得带上selenium就行
submit = driver.find_element_by_id('submit') # 定位到"发表评论"的按钮
submit.click() # 点击“发表评论”按钮
driver.close()


# 下面是只能在你的本地运行的答案：
from selenium import  webdriver # 从selenium模块中调用webdriver模块
import time

driver = webdriver.Chrome() # 声明浏览器为本地的Chrome
driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php') # 访问页面
time.sleep(1) # 暂停两秒，等待浏览器缓冲

username = driver.find_element_by_id('user_login') # 定位到输入用户名的位置
username.send_keys('spiderman') # 输入用户名
password = driver.find_element_by_id('user_pass') # 定位到输入密码的位置
password.send_keys('crawler334566') # 输入密码
login = driver.find_element_by_id('wp-submit') # 定位到登录按钮的位置
login.click() # 点击登录
time.sleep(2) # 等待两秒

article = driver.find_element_by_partial_link_text('三') # 根据链接的部分文字"三"，定位到这个链接
article.click() # 点击链接
time.sleep(1) # 等待一秒
comment = driver.find_element_by_id('comment') # 定位到评论区
comment.send_keys('蜘蛛侠的selenium评论') # 输入评论内容，随意发挥你的创意，记得带上selenium就行
submit = driver.find_element_by_id('submit') # 定位到"发表评论"的按钮
submit.click() # 点击“发表评论”按钮
driver.close()
 