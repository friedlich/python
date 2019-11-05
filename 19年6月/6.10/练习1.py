import requests

destnation_url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md'
res = requests.get (destnation_url) 
print(res.status_code) # 查看响应码
res.encoding = 'utf-8'
article=res.text # 把Response对象的内容以字符串的形式返回
#print(article)
with open('文章.txt','a') as f:
    f.write(article) 