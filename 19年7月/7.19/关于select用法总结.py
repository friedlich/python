# BeautifulSoup select()/select_one() 用法总结：
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
##
# 使用 select()/select_one() 时，标签名不加任何修饰，类名前加点，id名前加 #，属性用 [属性=’xxxx’]。
# select() 返回类型是 list。
# select_one() 返回值是list的首个。

# 设置字符集，导入包
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
soup = bs.select('...')
# （1）通过标签名查找
link_node = soup.select_one('a')
print('通过标签查标签名:   '+link_node.name)
#通过标签查标签名:   a

print(soup.select('b'))
#[<b>The Dormouse's story</b>]

# （2）通过类名查找
link_node = soup.select_one('.sister')
print('通过class查href:   '+link_node.get('href'))
#通过class查href:   http://example.com/elsie

print(soup.select('.sister'))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 结果为一个list，如果需要取出里面元素信息，需要用 for 循环

# （3）通过 id 名查找
link_node = soup.select_one('#link1')
print('通过id查内容:   '+link_node.text)
#通过id查内容:   Elsie

print(soup.select('#link1'))
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

# （4）组合查找
# 查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
link_node = soup.select_one('p #link1')
print(link_node)
#<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

#获取结果中的class
print(link_node.get('class'))
#['sister']
#这里注意，获取class返回是个list，其他的均为str、int

#获取结果中的href
print(link_node.get('href'))
#http://example.com/elsie

# 直接子标签查找
print(soup.select("head > title"))
#[<title>The Dormouse's story</title>]

# （5）属性查找
# 查询可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
#查a标签下 带有属性为http://example.com/tillie的结果，注意，这里是同一个节点
link_node = soup.select_one('a[href="http://example.com/tillie"]')
print('通过组合标签和属性查找内容：   '+link_node.text)
#通过组合标签和属性查找内容：   Tillie

#p标签下 带有href属性为http://example.com/tillie的结果，注意，这里是子节点
link_node = soup.select_one('p [href="http://example.com/tillie"]')
print(link_node.text)
#Tillie




