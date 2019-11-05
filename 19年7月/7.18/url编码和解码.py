# Python进行URL解码
# 所用模块：urllib
# 所用函数：urllib.unquote()
from urllib.request import quote, unquote
# import urllib # 这样不行
rawurl = "%E6%B2%B3%E6%BA%90"
url = unquote(rawurl)
print(url)
print(quote("河源"))
print(type(quote('河源')))
# URL为何要编码、解码？
# 通常如果一样东西需要编码，说明这样东西并不适合传输。原因多种多样，如Size过大，包含隐私数据。对于Url来说，之所以要进行编码，
# 是因为Url中有些字符会引起歧义。
# 例如，Url参数字符串中使用key=value键值对这样的形式来传参，键值对之间以&符号分隔，如/s?q=abc&ie=utf-8。如果你的value字符串中
# 包含了=或者&，那么势必会造成接收Url的服务器解析错误，因此必须将引起歧义的&和=符号进行转义，也就是对其进行编码。
# 又如，Url的编码格式采用的是ASCII码，而不是Unicode，这也就是说你不能在Url中包含任何非ASCII字符，例如中文。否则如果客户端浏览器
# 和服务端浏览器支持的字符集不同的情况下，中文可能会造成问题。


# -*- coding: utf-8 -*-

# @File    : urldecode_demo.py
# @Date    : 2018-05-11

from urllib.request import quote, unquote

# 编码

url1 = "https://www.baidu.com/s?wd=中国"

# utf8编码，指定安全字符
ret1 = quote(url1, safe=";/?:@&=+$,", encoding="utf-8")
print(ret1)
print(type(ret1))
# https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD

# gbk编码
ret2 = quote(url1, encoding="gbk")
print(ret2)
print(type(ret2))
# https%3A//www.baidu.com/s%3Fwd%3D%D6%D0%B9%FA


# 解码
url3 = "https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD"
print(unquote(url3))

url4 = 'https%3A//www.baidu.com/s%3Fwd%3D%D6%D0%B9%FA'
print(unquote(url4, encoding='gbk'))

