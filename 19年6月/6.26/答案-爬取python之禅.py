# 正确答案
# 具体的方法都写在了代码注释中。  
# 由于教学系统中与你本地的浏览器设置方法不同，我给你提供了两份答案，一份可以在课程系统中运行，一份可以在你的本地运行。


# # 下面是只能在爬虫课系统中运行的答案：
# from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# from bs4 import BeautifulSoup
# import time

# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome设置为静默模式
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 设置浏览器引擎为远程浏览器

# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
# time.sleep(2) # 暂停两秒，等待浏览器缓冲

# teacher = driver.find_element_by_id('teacher') # 定位到【请输入你喜欢的老师】下面的输入框位置
# teacher.send_keys('必须是吴枫呀') # 输入文字
# assistant = driver.find_element_by_name('assistant') # 定位到【请输入你喜欢的助教】下面的输入框位置
# assistant.send_keys('都喜欢') # 输入文字
# button = driver.find_element_by_class_name('sub') # 定位到【提交】按钮
# button.click() # 点击【提交】按钮
# time.sleep(1) # 等待一秒

# pageSource = driver.page_source # 获取页面信息
# soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
# contents = soup.find_all(class_="content") # 找到源代码Python之禅中文版和英文版所在的元素
# for content in contents:  # 遍历列表
#     title = content.find('h1').text # 提取标题
#     chan = content.find('p').text.replace('  ','') # 提取Python之禅的正文，并且去掉文字前面的所有空格
#     print(title + chan + '\n') # 打印Python之禅的标题与正文
# driver.close()


# 下面是只能在你的本地运行的答案：
from selenium import  webdriver # 从selenium库总调用webdriver模块
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome() # 声明浏览器对象
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher') # 定位到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant') # 定位到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub') # 定位到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(1) # 等待一秒

pageSource = driver.page_source # 获取页面信息
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
contents = soup.find_all(class_="content") # 找到源代码Python之禅中文版和英文版所在的元素
for content in contents:  # 遍历列表
    title = content.find('h1').text # 提取标题
    chan = content.find('p').text.replace('  ','') # 提取Python之禅的正文，并且去掉文字前面的所有空格
    print(title + chan + '\n') # 打印Python之禅的标题与正文
driver.close()
  