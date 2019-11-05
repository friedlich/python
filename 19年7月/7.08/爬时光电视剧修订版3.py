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
            TV_title = i.find(class_="px14").text.split()[0]
            datas = i.find(class_="mov_con").find_all('p')
            p_len = len(datas)
            p_first = datas[0].text
            derector = ''
            actor = ''
            info = ''
            if p_len == 1:
                if p_first[0] == '导':
                    derector = datas[0].text.replace('导演： ','')
                elif p_first[0] == '主':
                    actor = datas[0].text.replace('主演： ','')
                else:
                    info = p_first
            elif p_len == 2:
                if p_first[0] == '导':
                    derector = datas[0].text.replace('导演： ','')
                    if '主演： ' in datas[1].text:
                        actor = datas[1].text.replace('主演： ','')
                    else:
                        info = datas[1].text
                else:
                    actor = datas[0].text.replace('主演： ','')
                    info = datas[1].text
            else:
                derector = datas[0].text.replace('导演： ','')
                actor = datas[1].text.replace('主演： ','')
                info = datas[2].text
            writer.writerow([TV_num,TV_title,derector,actor,info])

csv_file = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/19年6月/6.30/shiguang7.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['序号','剧名','导演','主演','简介'])

task_list = []
for i in range(4):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
print(end-start)
