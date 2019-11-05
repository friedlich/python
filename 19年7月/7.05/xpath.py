from selenium import  webdriver # 从selenium库总调用webdriver模块
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome() # 声明浏览器对象
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_xpath('//*[@id=\"teacher\"]') # 定位到【请输入你喜欢的老师】下面的输入框位置
# //*[@id="teacher"] 没注意加了\这个麽 因为引号在python里表示字符串，所以为了区别，里面的引号外面要加\ 可是我试过不加\也行...
# 双引转义能不能依靠前面加个r呢 可以 这一句xpath是唯一的么 对滴 xpath是唯一的 直接右键copy，不比你一个个找标签方便吗
# xpath完事儿了嗷 在取大量标签数据，像豆瓣时还是bs方便 正则，bs，xpath三种提取数据的方法，那种优势呢
# 从电脑运行效率来讲,正则>bs>xpath;从使用简单来讲正则<bs<xpath 我的理解是，单个数据用xpath，集体的数据选择bs，都不行来正则 
# 所以,有大神能告诉我一下,用xpath的时候,那个\到底是书写格式,还是转义符 是转义符,如果不转义，就认定字符串了 嗯，了解
teacher.send_keys('必须是琦玉呀') # 输入文字
assistant = driver.find_element_by_xpath('//*[@id=\"assistant\"]') # 定位到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_xpath('//*[@id=\"div2\"]/div/form/input[3]') # 定位到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(1) # 等待一秒

### 方法一
sentence1 = driver.find_element_by_xpath('/html/body/div[3]/div[1]')
print(type(sentence1))
print(sentence1.text)
sentence2 = driver.find_element_by_xpath('/html/body/div[3]/div[2]')
print(type(sentence2))
print(sentence2.text)

driver.close()


### 方法二
# sentences = driver.find_elements_by_class_name('content')
# for sentence in sentences:
#     title = sentence.find_element_by_tag_name('h1').text
#     print(type(title))
#     content = sentence.find_element_by_id('p').text.strip()
#     print(type(content))
#     print(title + '\n' + content + '\n')

# driver.close()

### 方法三
# pageSource = driver.page_source # 获取页面信息
# soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
# contents = soup.find_all(class_="content") # 找到源代码Python之禅中文版和英文版所在的元素
# for content in contents:  # 遍历列表
#     title = content.find('h1').text # 提取标题
#     chan = content.find('p').text.replace('  ','') # 提取Python之禅的正文，并且去掉文字前面的所有空格
#     print(title + chan + '\n') # 打印Python之禅的标题与正文
# driver.close()