import requests #调用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html') 
#获取网页源代码，得到的res是response对象
print(res.status_code) #检查请求是否正确响应
html = res.text #把res的内容以字符串的形式返回
print(html)#打印html