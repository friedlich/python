params = input('请把要转换格式的params参数黏贴到这里：')
from urllib.request import quote,unquote
import re
list = []
res = unquote(params,encoding='utf-8')
print(res)
add = unquote(params,encoding='gbk')
print(add)
# utf = quote(res,encoding='utf-8')
# print(utf)
# gb = quote(res,encoding='gbk')
# print(gb)
res1 = re.split('&',res)
print(res1)
for i in res1:
    res2 = re.split('=',i)
    key = res2[0]
    try:
        value = res2[1]
    except IndexError:
        value = ''
    list.append((key,value))
print(list)
dict = dict(list)
print(dict)
#  nobase64=1&musicid=97773&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0