# 官方文档已经讲得非常详细：见图解

# 大概意思是，按照标准，URL只允许一部分ASCII字符，其他字符（如汉字）是不符合标准的，此时就要进行编码。
# 因为我在构造URL的过程中要使用到中文：
# "Param": "全文检索:*", # 搜索关键字
# 所以此时要对它进行编码操作：
from urllib import parse
string = "全文搜索"
print(parse.quote(string))

# urllib.parse解析 url:urllib.parse.urlparse(url, scheme='', allow_fragments=True)
# 简单的使用：urlparse
from urllib import parse #解析url 
print(parse.urlparse('https://movie.douban.com/')) 
print(parse.urlparse('https://movie.douban.com/', scheme='http')) 
print(parse.urlparse('movie.douban.com/', scheme='http')) 
# 下面是结果 
# ParseResult(scheme='https', netloc='movie.douban.com', path='/', params='', query='', fragment='') 
# ParseResult(scheme='https', netloc='movie.douban.com', path='/', params='', query='', fragment='') 
# ParseResult(scheme='http', netloc='', path='movie.douban.com/', params='', query='', fragment='')
# 可以看出加了scheme参数和没加的返回结果是有区别的。而当scheme协议加了，而前面的url也包含协议，一般会忽略后面的scheme参数

# 既然有解析url，那当然也有反解析url，就是把元素串连成一个url
from urllib import parse # 将列表元素拼接成url 
url = ['http', 'www', 'baidu', 'com', 'dfdf', 'eddffa'] # 这里至少需要6个元素 
print(parse.urlunparse(url)) 
# urlunparse()接收一个列表的参数，而且列表的长度是有要求的，是必须六个参数以上，要不会抛出异常

# urllib.parse.urljoin():这个是将第二个参数的url缺少的部分用第一个参数的url补齐
# 连接两个参数的url, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主
print(parse.urljoin('https://movie.douban.com/', 'index'))
print(parse.urljoin('https://movie.douban.com/', 'https://accounts.douban.com/login'))

# urlencode
# urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串，比如：
from urllib.parse import urlencode
data = {
     'a': 'test',
     'name': '魔兽'
 }
print(urlencode(data))
# a=test&amp;name=%C4%A7%CA%DE
# 如果只想对一个字符串进行urlencode转换，怎么办？urllib提供另外一个函数：quote()
from urllib.parse import quote
print(quote('魔兽'))

# urldecode
# 当urlencode之后的字符串传递过来之后，接受完毕就要解码了——urldecode。urllib提供了unquote()这个函数，可没有urldecode()
from urllib.parse import unquote
# unquote('%C4%A7%CA%DE')
print(unquote('%C4%A7%CA%DE',encoding='gb2312'))
print(unquote('%C4%A7%CA%DE',encoding='GBK'))
print(unquote('%C4%A7%CA%DE',encoding='utf-8')) # 这个怎么就不行了呢





