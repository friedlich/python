import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res =requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 返回一个response对象，赋值给res
html=res.text #超文本标记语言
# 把res解析为字符串
soup = BeautifulSoup( html,'html.parser')
# 把网页解析为BeautifulSoup对象
print(type(soup)) # <class 'bs4.BeautifulSoup'>
items = soup.find_all(class_='books')   # 通过匹配属性class='books'提取出我们想要的元素
print(type(items)) #元素.结果集 <class 'bs4.element.ResultSet'>
print('\n')
for item in items:                      # 遍历列表items
    print(type(item)) #元素.标签 <class 'bs4.element.Tag'>
    kind = item.find('h2')               # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='title')     #  在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info')      # 在列表中的每个元素里，匹配属性class_='info'提取出数据
    print(type(kind),type(title),type(brief)) # 打印提取出的数据类型
    print(kind,'\n',title,'\n',brief) # 打印提取出的数据
    print('\n')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text) # 打印书籍的类型、名字、链接和简介的文字
    print('\n')
