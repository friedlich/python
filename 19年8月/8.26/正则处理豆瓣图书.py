import requests
import re

response = requests.get('https://book.douban.com/')
print(response.status_code)
content = response.text
# print(content)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)"',re.S)
print(type(pattern))
results = re.findall(pattern,content)
print(type(results))
print(results)
# for result in results:
#     url,name,author,data = result
#     author = re.sub('\s','',result)
#     data = re.sub('\s','',data)
#     print(url,name,author,data)
