import requests
from bs4 import BeautifulSoup
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get (url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.find_all('div') #用find_all()把所有符合要求的数据提取出来，并放在变量items里
print(type(items)) #打印items的数据类型
print(items)       #打印items

# 运行结果是那三个<div>元素，它们一起组成了一个列表结构。打印items的类型，显示的是<class 'bs4.element.ResultSet'>，
# 是一个ResultSet类的对象。其实是Tag对象以列表结构储存了起来，可以把它当做列表来处理。