import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
print(type(res.text))
soup = BeautifulSoup( res.text,'html.parser')
print(type(soup)) #查看soup的类型
# print(soup) # 打印soup

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(字符串,'html.parser')