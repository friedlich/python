import requests 
#调用requests模块
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html') 
#获取网页源代码，得到的res是response对象。
print(res.status_code) 
res.encoding = 'utf-8'
code = res.text
#检查请求是否正确响应
#print(res.text) 
#打印网页源代码的文本

with open('code.txt','a',encoding='utf-8') as f:
    f.write(code)