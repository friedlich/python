from gevent import monkey
monkey.patch_all()
import gevent,requests,bs4,csv
from gevent.queue import Queue

work = Queue()
url_1 = 'http://www.boohee.com/food/group/{num1}?page={num2}'
for i in range(1,4):
    for x in range(1,4):
        real_url = url_1.format(num1=i,num2=x)
        work.put_nowait(real_url)
url_2 = 'http://www.boohee.com/food/view_menu?page={num3}'
for i in range(1,4):
    real_url = url_2.format(num3=i)
    work.put_nowait(real_url)
    
def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers = headers)
        bsdata = bs4.BeautifulSoup(res.text,'html.parser')
        datas = bsdata.find_all(class_="item clearfix")
        for i in datas:
            name = i.find('h4').text
            heat = i.find('p').text
            href = i.find('a')['href']
            print([name,heat,href])
task_list = []
for i in range(4):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)