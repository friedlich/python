#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。

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
        datas = bsdata.find_all(class_="mov_con")
        for i in datas:
            TV_title = i.find(class_="px14").text
            data = i.find_all('p')
            director = ''
            actor = ''
            for p in data:
                if str(p).__contains__('导演： '):  # __contains__判断字符串中是否包含相应的字符。
                    director = p.text.replace('导演： ','')  
                elif str(p).__contains__('主演： '):
                    actor = p.text.replace('主演： ','')
            infor = i.find(class_="mt3")
            if infor != None:
                info = infor.text
            else:
                info = ''          
            # TV_data = ''
            # for x in data:
            #     TV_data = TV_data + '' + x.text
            # writer.writerow([TV_title,TV_data])
            writer.writerow([TV_title,director,actor,info])
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





            

