from urllib.parse import quote
keyword = '奥迪'
kwd = quote(keyword, encoding='utf-8', errors='replace')
print(kwd)
kwd = quote(keyword, encoding='gbk', errors='replace')
print(kwd)

from urllib.parse import quote
import string
#
url = r'http://www.xxxx.com/name=锂电池+氢气'
url = quote(url, safe=string.printable)  # safe表示可以忽略的字符
print(quote(url))
print(url)
