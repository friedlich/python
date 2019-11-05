from pyquery import PyQuery as pq
doc = pq(url='http://www.baidu.com')
print(doc('head'))