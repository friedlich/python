from bs4 import BeautifulSoup

bs = BeautifulSoup('<p><a href=\'https://www.pypypy.cn\'></a></p>','html.parser')
# 此处多出来的\，是转义字符。
tag = bs.find('p')
print(tag['href'])
# 这样会报错，因为<p>标签没有属性href，href属于<a>标签