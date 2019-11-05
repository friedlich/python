from selenium import  webdriver 
import time

driver = webdriver.Chrome() 

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
# print(type(driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') ))
time.sleep(2) # 等待2秒
# 用time.sleep(2)等待两秒，是由于浏览器缓冲加载网页需要耗费一些时间，以及我在这个网页中设置了一秒之后才从首页跳转到输入
# 页面，所以，等待两秒再去解析和提取比较稳妥。

label = driver.find_element_by_tag_name('label') # 解析网页并提取第一个<lable>标签
print(type(label))
print(label.text) # 打印label的文本
print(label)

driver.close() # 关闭浏览器