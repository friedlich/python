import urllib
from urllib.parse import quote # 这里下面的的报错就很奇怪，必须要用from引入quote才可以

book_name = input('输入你想查询的小说名称')
# url = 'http://www.biquge.cm/modules/article/sou.php?searchkey=' + quote(book_name.encode('gb2312'))
# print(url)
print('http://www.biquge.cm/modules/article/sou.php?searchkey=' + urllib.parse.quote(book_name.encode('gb2312')))
## AttributeError: module 'urllib' has no attribute 'parse'
url ='http://www.biquge.cm/3/3095/1749160.html'
print(url[url.find('/', 1)])
print(url[url.rfind('/', 1)])
print(url[url.find('/', 1) + 1:-5])
print(url[url.find('/', 0) + 1:-5])
print(url[url.find('/', 2) + 1:-5])
print(url[url.rfind('/', 1) + 1:-5])
print(url[url.rfind('/', 0) + 1:-5])
print(url[url.rfind('/', 50) + 1:-5])
# rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
# str.rfind(str, beg=0 end=len(string))
    # str -- 查找的字符串
    # beg -- 开始查找的位置，默认为 0
    # end -- 结束查找位置，默认为字符串的长度。
## 返回字符串最后一次出现的位置，如果没有匹配项则返回-1

#!/usr/bin/python

str = "this is really a string example....wow!!!";
substr = "is";
print(str.rfind(substr))
print(str.rfind(substr, 0, 10))
print(str.rfind(substr, 10, 0))
print(str.find(substr))
print(str.find(substr, 0, 10))
print(str.find(substr, 10, 0))
