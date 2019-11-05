from gevent import monkey
monkey.patch_all()
import gevent,requests,time,csv
from gevent.queue import Queue
from bs4 import BeautifulSoup

start = time.time()
work = Queue()

url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)

url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for i in range(2,11):
    real_url = url_2.format(page=i)
    work.put_nowait(real_url)

def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        bsdata = BeautifulSoup(res.text,'html.parser')
        content = bsdata.find(id="asyncRatingRegion").find_all('li')
        for i in content:
            TV_num = i.find(class_="number").text
            TV_title = i.find(class_="px14").text
            datas = i.find(class_="mov_con").find_all('p')
            list = [TV_num,TV_title,'','','']
            for p in datas:
                if '导演： ' in str(p):
                    list[2] = p.text.replace('导演： ','')
                elif '主演： ' in str(p):
                    list[3] = p.text.replace('主演： ','')
                else:
                    list[4] = p.text                      
            writer.writerow(list)
csv_file = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/19年6月/6.30/shiguang6.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['序号','剧名','导演','主演','简介'])

task_list = []
for i in range(4):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
print(end-start)