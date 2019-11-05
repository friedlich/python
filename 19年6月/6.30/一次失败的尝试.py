from gevent import monkey
monkey.patch_all()
import gevent,time,requests

start = time.time()
url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/'
'……'
]
#假设有1000个网址

def crawler(url_list):
#定义一个crawler()函数。
    for url in url_list:
        r = requests.get(url)
        print(url,time.time()-start,r.status_code)

tasks_list = [ ]
#创建空的任务列表。
for i in range(5):
    task = gevent.spawn(crawler,url_list[i*200:(i+1)*200])
    #用gevent.spawn()函数创建5个任务。
    tasks_list.append(task)
    #往任务列表添加任务。

gevent.joinall(tasks_list)
end = time.time()
print(end-start)

# 遗憾地告诉你，这么做也还是会有问题的。就算我们用gevent.spawn()创建了5个分别执行爬取200个网站的任务，这5个任务之间是异步执行的，但是每个任务（爬取200个网站）内部是同步的。

# 这意味着：如果有一个任务在执行的过程中，它要爬取的一个网站一直在等待响应，哪怕其他任务都完成了200个网站的爬取，它也还是不能完成200个网站的爬取。