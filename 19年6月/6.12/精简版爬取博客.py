import requests
from bs4 import BeautifulSoup

html = requests.get('https://spidermen.cn/')
soup = BeautifulSoup(html.text,'html.parser')
print(type(soup))
items = soup.find_all(class_="entry-header")
print(type(items))
for item in items:
    title = item.find(class_="entry-title")
    print(type(title))
    time = item.find(class_="entry-date published")
    http = item.find(rel="bookmark")
    print(title.text,'发布于：',time.text)
    print(http['href'])