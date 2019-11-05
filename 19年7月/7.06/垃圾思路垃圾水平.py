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
movie_list = []
def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        bsdata = BeautifulSoup(res.text,'html.parser')
        movie_con = bsdata.find_all(class_="mov_con")
        movie_num = bsdata.find_all(class_="number")
        for b in range(len(movie_con)):
            movie_name = movie_con[b].find(class_="px14")
            movie_p = movie_con[b].find_all('p')
            num_rank = int(movie_num[b].text)
            movie_list[num_rank] = [movie_num.text]
            for c in range(len(movie_p)):
                movie_list[num_rank].append(movie_p[c].text)
            # TV_data = ''
            # for x in data:
            #     TV_data = TV_data + '' + x.text
            # writer.writerow([TV_title,TV_data])
csv_file = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/19年6月/6.30/shiguang4.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['剧名','导演','主演','简介'])

task_list = []
for i in range(4):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
print(end-start)